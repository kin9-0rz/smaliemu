# -*- coding: utf-8 -*-
# This file is part of the Smali Emulator.
#
# Copyright(c) 2016 Simone 'evilsocket' Margaritelli
# evilsocket@gmail.com
# http://www.evilsocket.net
#
# This file may be licensed under the terms of of the
# GNU General Public License Version 3 (the ``GPL'').
#
# Software distributed under the License is distributed
# on an ``AS IS'' basis, WITHOUT WARRANTY OF ANY KIND, either
# express or implied. See the GPL for the specific language
# governing rights and limitations.
#
# You should have received a copy of the GPL along with this
# program. If not, go to http://www.gnu.org/licenses/gpl.html
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
import sys
import time

from smaliemu.opcodes import *
from smaliemu.vm import VM
from smaliemu.source import Source
from smaliemu.snippet import Snippet
from smaliemu.preprocessors import TryCatchPreprocessor
from smaliemu.preprocessors import PackedSwitchPreprocessor
from smaliemu.preprocessors import ArrayDataPreprocessor
from smaliemu.exception import UnsupportedOpcodeError


# Holds some statistics.
class Stats(object):

    def __init__(self, vm):
        self.opcodes = len(vm.opcodes)
        self.preproc = 0
        self.execution = 0
        self.steps = 0

    def __repr__(self):
        s = "opcode handlers    : %d\n" % self.opcodes
        s += "preprocessing time : %d ms\n" % self.preproc
        s += "execution time     : %d ms\n" % self.execution
        s += "execution steps    : %d\n" % self.steps
        return s


# The main emulator class.
class Emulator(object):

    def __init__(self):
        # Instance of the virtual machine.
        self.vm = None
        # Instance of the source file.
        self.source = None
        self.snippet = None
        # Instance of the statistics object.
        self.stats = None
        # Code preprocessors.
        self.preprocessors = [
            TryCatchPreprocessor, PackedSwitchPreprocessor,
            ArrayDataPreprocessor
        ]
        # Opcodes handlers.
        self.opcodes = []

        # Dynamically load opcode handlers.
        # TODO: Implement missing opcodes.
        for entry in dir(sys.modules['smaliemu.opcodes']):
            if entry.startswith('op_'):
                self.opcodes.append(globals()[entry]())

    def __preprocess(self, smali_code):
        """
        Start the preprocessing phase which will save all the labels and their
        line index for fast lookups while jumping and will pre parse all the
        try/catch directives.
        """
        next_line = None
        smali_code.lines = list(map(str.strip, smali_code.lines))
        for index, line in enumerate(smali_code.lines):
            # we're inside a block which was already processed
            if next_line is not None and index <= next_line:
                next_line = None if index == next_line else next_line
                continue
            elif line == '':  # skip empty lines
                continue
            elif line[0] == ':':  # we've found something to preprocess
                # loop each preprocessors and search for the one responsible
                # to parse this line
                processed = False
                for preproc in self.preprocessors:
                    if preproc.check(line):
                        next_line = preproc.process(self.vm, line, index,
                                                    smali_code.lines)
                        processed = True

                # no preprocessor found, this is a normal label
                if processed is False:
                    self.vm.labels[line] = index

    def __parse_line(self, line):
        # Search for appropriate parser.
        for parser in self.opcodes:
            if parser.parse(line, self.vm):
                return True

        return False

    @staticmethod
    def __should_skip_line(line):
        """
        Helper method used to determine if a line must be skipped/ignored.
        :param line: The line to check.
        :return: True if the line can be ignored, otherwise False.
        """
        return line == "" or line[0] == '#' or line[0] == ':' or line[0] == '.'

    def fatal(self, message):
        """
        Display an error message, the current line being executed and quit.
        :param message: The error message to display.
        """
        print()
        print("-------------------------")
        print("Fatal error on line %03d:\n" % self.vm.pc)
        if self.source:
            print("  %03d %s" % (self.vm.pc, self.source[self.vm.pc - 1]))
        elif self.snippet:
            print("  %03d %s" % (self.vm.pc, self.snippet[self.vm.pc - 1]))

        print("\n%s" % message)

    def get_error_line(self):
        if self.source:
            return "  %03d %s" % (self.vm.pc, self.source[self.vm.pc - 1])
        elif self.snippet:
            return "  %03d %s" % (self.vm.pc, self.snippet[self.vm.pc - 1])

    def run(self, filename, args={}, trace=False):
        """
        Load a smali file and start emulating it.
        :param filename: The path of the file to load and emulate.
        :param args: A dictionary of optional initialization variables for the
                     VM, mostly used for arguments.
        :param trace: If true every opcode being executed will be printed.
        :return: The return value of the emulated method or None if no return-*
                 opcode was executed.
        """
        OpCode.trace = trace
        self.source = Source(filename)
        self.vm = VM(self)
        self.stats = Stats(self)

        self.vm.variables.update(args)

        s = time.time() * 1000
        # Preprocess labels and try/catch blocks for fast lookup.
        self.__preprocess(self.source)
        e = time.time() * 1000
        self.stats.preproc = e - s

        s = time.time() * 1000
        # Loop each line and emulate.
        while self.vm.stop is False and self.source.has_line(self.vm.pc):
            self.stats.steps += 1
            line = self.source[self.vm.pc]
            self.vm.pc += 1

            if self.__should_skip_line(line):
                continue

            elif self.__parse_line(line) is False:
                raise UnsupportedOpcodeError(self.get_error_line())

        e = time.time() * 1000
        self.stats.execution = e - s

        return self.vm.return_v

    def call(self, snippet, args={}, trace=False, thrown=True):
        """
        Load a smali file and start emulating it.
        :param snippet: codes snippet in smali format
        :param trace: If true every opcode being executed will be printed.
        :param thrown: If error, emu will raise exception.
        :return: The return value of the emulated method or None if no return-*
                 opcode was executed.
        """

        OpCode.trace = trace
        self.snippet = Snippet(snippet)
        self.vm = VM(self)
        self.stats = Stats(self)
        self.vm.return_v = None
        self.vm.thrown = thrown

        self.vm.variables.update(args)

        self.vm.variables.copy()

        s = time.time() * 1000
        # Preprocess labels and try/catch blocks for fast lookup.
        self.__preprocess(self.snippet)
        e = time.time() * 1000
        self.stats.preproc = e - s

        s = time.time() * 1000
        # Loop each line and emulate.
        while self.vm.stop is False and self.snippet.has_line(self.vm.pc):
            self.stats.steps += 1
            line = self.snippet[self.vm.pc]
            self.vm.pc += 1

            if self.__should_skip_line(line):
                continue

            elif self.__parse_line(line) is False and thrown:
                raise UnsupportedOpcodeError(self.get_error_line())

        e = time.time() * 1000
        self.stats.execution = e - s

        return self.vm.return_v
