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
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from smaliemu.emulator import Emulator

emu = Emulator()

filename = os.path.join(os.path.dirname(__file__), 'decryptor.smali')

# Arguments for the method.
# args = {
#     'p0': (-62, -99, -106, -125, -123, -105, -98, -37, -105, -97, -103, -41, -118, -97, -113, -103, -109, -104, -115, 111, 98, 103, 35, 52),
#     'p1': 19
# }

# ret = emu.run(filename, args)
# print(emu.stats)
# print("RESULT: %s" % ret)
# print('-' * 100)

emu2 = Emulator()

filename = os.path.join(os.path.dirname(__file__), 'test.smali')
ret = emu2.run(filename, trace=True)
print(ret)
print(emu2.vm.variables)
exit()

snippet = [
    'const/16 v5, 0x29',
    'new-array v0, v5, [B',
    'fill-array-data v0, :array_66',
    'sput-object v0, xbd:[B',
    'const/16 v0, 0xde',
    'sput v0, xba:I',
    'new-instance v0, Ljava/lang/StringBuilder;',
    'sget-object v1, xbd:[B',
    'const/4 v2, 0x6',
    'aget-byte v1, v1, v2',
    'int-to-byte v1, v1',
    'or-int/lit8 v2, v1, 0x50',
    'int-to-byte v2, v2',
    'sget-object v3, xbd:[B',
    'const/16 v4, 0x13',
    'aget-byte v3, v3, v4',
    'int-to-byte v3, v3',
    'return-object v0',
    ':array_66',
    '   .array-data 1',
    '       0x79t',
    '       -0x52t',
    '       0x16t',
    '       0x47t',
    '       0xet',
    '       0x2t',
    '       0x5t',
    '       0xct',
    '       0x7t',
    '       0x8t',
    '       0x4t',
    '       0x5t',
    '       0x16t',
    '       0x8t',
    '       0x4bt',
    '       -0x46t',
    '       0xft',
    '       -0x7t',
    '       0x7t',
    '       0x19t',
    '       0x1t',
    '       0x9t',
    '       0x4ct',
    '       -0x4dt',
    '       0x2t',
    '       0x10t',
    '       0x12t',
    '       0x32t',
    '       0x21t',
    '       0x13t',
    '       -0x1t',
    '       -0x36t',
    '       -0xct',
    '       0xft',
    '       0x12t',
    '       0x9t',
    '       -0xat',
    '       0x16t',
    '       0x8t',
    '       0x31t',
    '       0x21t',
    '   .end array-data'
]


ret = emu2.call(snippet, trace=True)
print("'%s'" % ret)
