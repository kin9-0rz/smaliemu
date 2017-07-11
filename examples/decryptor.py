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
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from smaliemu.emulator import Emulator

emu = Emulator()

filename = os.path.join( os.path.dirname(__file__), 'decryptor.smali' )

# Arguments for the method.
args = {
    'p0': (-62, -99, -106, -125, -123, -105, -98, -37, -105, -97, -103, -41, -118, -97, -113, -103, -109, -104, -115, 111, 98, 103, 35, 52),
    'p1': 19
}

# ret = emu.run(filename, args)
# print(emu.stats)
# print("RESULT:\n")
# print("'%s'" % ret)

emu2 = Emulator()
#
# snippet = ['const/4 v1, 0x0', 'const-string v2, "z"', 'invoke-virtual {v2, v1}, Ljava/lang/String;->charAt(I)C']
# ret = emu2.call(snippet)
# print("'%s'" % ret)
#
# snippet = [
#     'const/4 v4, 0x1',
#     'const/4 v3, 0x0',
#     'new-instance v0, Ljava/lang/String;',
#     'new-array v1, v4, [B',
#     'const/16 v2, 0x44',
#     'aput-byte v2, v1, v3',
#     'invoke-direct {v0, v1}, Ljava/lang/String;-><init>([B)V',
#     'return-object v0'
# ]
# ret = emu2.call(snippet)
# print("'%s'" % ret)

#
# snippet = [
#     'const/4 v4, 0x1',
#     'const/4 v3, 0x0',
#     'new-instance v0, Ljava/lang/String;',
#     'const/4 v1, 0x2',
#     'new-array v1, v1, [B',
#     'fill-array-data v1, :array_5a',
#     'invoke-direct {v0, v1}, Ljava/lang/String;-><init>([B)V',
#     'return-object v0',
#     ':array_5a',
#     '.array-data 1',
#         '0x44t',
#         '0x45t',
#     '.end array-data'
#
# ]
# ret = emu2.call(snippet)
# print("'%s'" % ret)

# snippet = [
#     'const/4 v4, 0x0',
#     'new-instance v4, Ljava/lang/StringBuilder;',
#     'const-string v5, "test_value_of"',
#     'invoke-static {v5}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;',
#     'move-result-object v5',
#     'invoke-direct {v4, v5}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V',
#     'return-object v4'
# ]
# ret = emu2.call(snippet)
# print("Result : %s\n" % ret)
#
snippet = [
    # 'const/4 v4, 0x0',
    'new-instance v4, Ljava/lang/StringBuilder;',
    'const-string v5, "a"',
    'invoke-static {v5}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;',
    'move-result-object v5',
    'invoke-direct {v4, v5}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V',
    'const-string v5, "h"',
    'invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;',
    'return-object v4'

]
ret = emu2.call(snippet)
print("Result : %s" % ret)
#
# import sys
# sys.exit()
#
# snippet = [
#     '    new-instance v4, Ljava/lang/StringBuilder;',
#     '    const-string v5, "c"',
#     '    invoke-static {v5}, Ljava/lang/String;->valueOf(Ljava/lang/Object;)Ljava/lang/String;',
#     '    move-result-object v5',
#     '    invoke-direct {v4, v5}, Ljava/lang/StringBuilder;-><init>(Ljava/lang/String;)V',
#     '    const-string v5, "h"',
#     '    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;',
#     '    move-result-object v4',
#     '    const-string v5, "e"',
#     '    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;',
#     '    move-result-object v4',
#     '    const-string v5, "c"',
#     '    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;',
#     '    move-result-object v4',
#     '    const-string v5, "k"',
#     '    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;',
#     '    move-result-object v4',
#     '    const-string v5, "e"',
#     '    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;',
#     '    move-result-object v4',
#     '    const-string v5, "r"',
#     '    invoke-virtual {v4, v5}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;',
#     '    move-result-object v4',
#     '    invoke-virtual {v4}, Ljava/lang/StringBuilder;->toString()Ljava/lang/String;',
#     '   return-object v4'
#     ]
#
# ret = emu2.call(snippet)
# print("'%s'" % ret)

# support move-object/from16
snippet = [
    'new-instance v13, Ljava/lang/StringBuilder;',
    'invoke-direct {v13}, Ljava/lang/StringBuilder;-><init>()V',
    'const-string v16, "h"',
    'move-object/from16 v0, v16',
    'invoke-virtual {v13, v0}, Ljava/lang/StringBuilder;->append(Ljava/lang/String;)Ljava/lang/StringBuilder;',
    'return-object v13'
    ]

ret = emu2.call(snippet, thrown=True)
for excep in emu2.vm.exceptions:
    print(excep)
print("'%s'" % ret)

# snippet = [
#     'const/4 v7, 0x2',
#     'const/16 v6, 0xc',
#     'const/4 v5, 0x7',
#     'const/4 v4, 0x1',
#     'const/16 v3, 0x11',
#     'const/16 v0, 0x13',
#     'new-array v0, v0, [B',
#     'const/4 v1, 0x0',
#     'const/16 v2, 0x36',
#     'aput-byte v2, v0, v1',
#     'aput-byte v6, v0, v4',
#     'aput-byte v4, v0, v7',
#     'const/4 v1, 0x3',
#     'const/16 v2, 0x1a',
#     'aput-byte v2, v0, v1',
#     'const/4 v1, 0x4',
#     'aput-byte v3, v0, v1',
#     'const/4 v1, 0x5',
#     'const/16 v2, 0xb',
#     'aput-byte v2, v0, v1',
#     'const/4 v1, 0x6',
#     'const/16 v2, 0x1a',
#     'aput-byte v2, v0, v1',
#     'const/16 v1, 0x4e',
#     'aput-byte v1, v0, v5',
#     'const/16 v1, 0x8',
#     'const/16 v2, 0x15',
#     'aput-byte v2, v0, v1',
#     'const/16 v1, 0xa',
#     'const/16 v2, 0x5c',
#     'aput-byte v2, v0, v1',
#     'const/16 v1, 0xb',
#     'const/16 v2, 0x1e',
#     'aput-byte v2, v0, v1',
#     'const/16 v1, 0x1e',
#     'aput-byte v1, v0, v6',
#     'const/16 v1, 0xd',
#     'const/16 v2, 0x5c',
#     'aput-byte v2, v0, v1',
#     'const/16 v1, 0xe',
#     'const/16 v2, 0x46',
#     'aput-byte v2, v0, v1',
#     'const/16 v1, 0xf',
#     'aput-byte v5, v0, v1',
#     'const/16 v1, 0x10',
#     'aput-byte v6, v0, v1',
#     'const/16 v1, 0xd',
#     'aput-byte v1, v0, v3',
#     'const/16 v1, 0x12',
#     'const/16 v2, 0x17',
#     'aput-byte v2, v0, v1',
#     'return-object v0'
# ]

snippet = ['',
'    .registers 8', '    const/4 v7, 0x2',
'    const/16 v6, 0xc',
'    const/4 v5, 0x7', '    const/4 v4, 0x1', '    const/16 v3, 0x11',
'    const/16 v0, 0x13',
'    new-array v0, v0, [B', '    const/4 v1, 0x0', '    const/16 v2, 0x36',
'    aput-byte v2, v0, v1',
'    aput-byte v6, v0, v4', '    aput-byte v4, v0, v7', '    const/4 v1, 0x3', '    const/16 v2, 0x1a',
'    aput-byte v2, v0, v1', '    const/4 v1, 0x4', '    aput-byte v3, v0, v1', '    const/4 v1, 0x5',
'    const/16 v2, 0xb', '    aput-byte v2, v0, v1', '    const/4 v1, 0x6', '    const/16 v2, 0x1a',
'    aput-byte v2, v0, v1', '    const/16 v1, 0x4e', '    aput-byte v1, v0, v5', '    const/16 v1, 0x8',
'    const/16 v2, 0x15', '    aput-byte v2, v0, v1', '    const/16 v1, 0xa', '    const/16 v2, 0x5c',
'    aput-byte v2, v0, v1', '    const/16 v1, 0xb', '    const/16 v2, 0x1e', '    aput-byte v2, v0, v1',
'    const/16 v1, 0x1e', '    aput-byte v1, v0, v6', '    const/16 v1, 0xd', '    const/16 v2, 0x5c',
'    aput-byte v2, v0, v1', '    const/16 v1, 0xe', '    const/16 v2, 0x46', '    aput-byte v2, v0, v1',
'    const/16 v1, 0xf', '    aput-byte v5, v0, v1', '    const/16 v1, 0x10',
'    aput-byte v6, v0, v1', '    const/16 v1, 0xd', '    aput-byte v1, v0, v3', '    const/16 v1, 0x12',
'    const/16 v2, 0x17', '    aput-byte v2, v0, v1', 'return-object v0']

ret = emu2.call(snippet, thrown=True)
for excep in emu2.vm.exceptions:
    print(excep)
print("'%s'" % ret)

snippet = [
    'const/16 v0, 0x13',
    'new-array v0, v0, [B',
    'sput-object v0, Lcom/a/e/b;->K:[B',
    'const/16 v0, 0xa',
    'return-object v0'
]

ret = emu2.call(snippet, trace=True, thrown=True)
for excep in emu2.vm.exceptions:
    print(excep)
print("'%s'" % ret)
