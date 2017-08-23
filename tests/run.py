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
from collections import OrderedDict
import sys
import os
import fnmatch
import time
import traceback
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from smaliemu.emulator import Emulator


def get_data_files(file_filter):
    file_list = []
    datapath = os.path.join(os.path.dirname(__file__), 'data')

    for root, _, filenames in os.walk(datapath):
        for filename in fnmatch.filter(filenames, '*.smali'):
            if file_filter is None or file_filter in filename:
                file_list.append(os.path.join(root, filename))

    return file_list


def run_data_file(data_file):
    emu = Emulator()
    ret = emu.run(data_file)
    outx = emu.vm.variables.copy()
    outx.update({'ret': ret})
    return str(OrderedDict(sorted(outx.items()))).replace('OrderedDict([(', '{').replace(')])', '}').replace("',", "':").replace("), (", ', ')


def get_desired_output(data_file):
    return open(data_file).read().split("\n")[0][1:].strip()


def ppassed():
    print("\x1b[32mPASSED\x1b[0m")


def pfail(expected, got):
    print("\x1b[31mFAILED\x1b[0m\n")
    print("  Expected : %s" % expected)
    print("  Got      : %s" % got)


def pexception():
    print("\x1b[31mFAILED\x1b[0m\nsdsdsd")
    print(traceback.format_exc())

if __name__ == '__main__':
    ffilter = sys.argv[1] if len(sys.argv) == 2 else None
    files = get_data_files(ffilter)
    total = len(files)
    passed = 0
    failed = 0
    exceptions = 0
    start = time.time() * 1000
    just = len(max(files, key=len))

    for datafile in files:
        sys.stdout.write("Testing %s : " % datafile.ljust(just))

        try:
            out = run_data_file(datafile)
            test = get_desired_output(datafile)

            if out == test:
                ppassed()
                passed += 1
            else:
                pfail(test, out)
                failed += 1

        except Exception:
            exceptions += 1

    elapsed = (time.time() * 1000) - start

    print("Total Tests : %d" % total)
    print("Passed      : %d" % passed)
    print("Failed      : %d ( %d exceptions )" % (failed, exceptions))
    print("Total Time  : %f ms" % elapsed)
    print("Average     : %f ms / test" % (elapsed / float(total)))
