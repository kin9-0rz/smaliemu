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
import re

# Base class for all Dalvik opcodes (see
# http://pallergabor.uw.hu/androidblog/dalvik_opcodes.html).


class OpCode(object):
    trace = False

    def __init__(self, expression):
        self.expression = re.compile(expression)

    @staticmethod
    def get_int_value(val):
        ptn = re.compile(r'-?0x\w+?[ts]')

        # handle comments
        if '#' in val:
            val = val.split('#')[0]

        if ptn.match(val):
            return int(val[:-1], 16)
        elif "0x" in val:
            return int(val, 16)

        return int(val)

    def parse(self, line, vm):
        m = self.expression.search(line)
        if m is None:
            return False

        try:
            self.eval(
                vm, *[x if x is not None else x for x in m.groups()])
        except Exception as e:
            if vm.thrown:
                raise e
            vm.exception(e)

            vm.result = None
            for key in m.groups():
                if key in vm.variables:
                    del vm.variables[key]
                    break

        if OpCode.trace is True:
            # if True:
            print("%03d %s" % (vm.pc, line))
            print('Registers : ', vm.variables)
            print('Result    : ', vm.result)
            print('Return    : ', vm.return_v)

        return True

    @staticmethod
    def eval(vm, *args):
        pass

class op_Const(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^const(/\d+)?\s+(.+),\s*(.+)')

    @staticmethod
    def eval(vm, _, vx, lit):
        vm[vx] = OpCode.get_int_value(lit)
        vm.result = vm[vx]


class op_ConstWide(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^const-wide(/\d+)? (.+),\s*(.+)')

    @staticmethod
    def eval(vm, _, vx, lit):
        vm[vx] = OpCode.get_int_value(lit)
        vm.result = vm[vx]


class op_ConstString(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^const-string(?:/jumbo)? (.+),\s*"(.*)"')

    @staticmethod
    def eval(vm, vx, s):
        vm[vx] = s
        vm.result = vm[vx]


class op_Move(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^move(-object)?[\/from16]* (.+),\s*(.+)')

    @staticmethod
    def eval(vm, _, vx, vy):
        vm[vx] = vm[vy]


class op_MoveResult(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^move-result(-object)? (.+)')

    @staticmethod
    def eval(vm, _, dest):
        vm[dest] = vm.result


class op_MoveException(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^move-exception (.+)')

    @staticmethod
    def eval(vm, vx):
        vm[vx] = vm.exceptions.pop()


class op_IfLe(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-le (.+),\s*(.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, vy, label):
        if vm[vx] <= vm[vy]:
            vm.goto(label)


class op_IfGe(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-ge (.+),\s*(.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, vy, label):
        if vm[vx] >= vm[vy]:
            vm.goto(label)


class op_IfGez(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-gez (.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, label):
        if vm[vx] >= 0:
            vm.goto(label)


class op_IfLtz(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-ltz (.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, label):
        if vm[vx] < 0:
            vm.goto(label)


class op_IfGt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-gt (.+),\s*(.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, vy, label):
        if vm[vx] > vm[vy]:
            vm.goto(label)


class op_IfGtz(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-gtz (.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, label):
        if vm[vx] > 0:
            vm.goto(label)


class op_IfLez(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-lez (.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, label):
        if vm[vx] <= 0:
            vm.goto(label)


class op_IfEq(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-eq (.+),\s*(.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, vy, label):
        if vm[vx] == vm[vy]:
            vm.goto(label)


class op_IfNe(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-ne (.+),\s*(.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, vy, label):
        if vm[vx] != vm[vy]:
            vm.goto(label)


class op_IfLt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-lt (.+),\s*(.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, vy, label):
        if vm[vx] < vm[vy]:
            vm.goto(label)


class op_IfEqz(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-eqz (.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, label):
        if vm[vx] == 0:
            vm.goto(label)


class op_IfNez(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^if-nez (.+),\s*(\:.+)')

    @staticmethod
    def eval(vm, vx, label):
        if vm[vx] != 0:
            vm.goto(label)


class op_ArrayLength(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'array-length (.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy):
        vm[vx] = len(vm[vy])


class op_ArrayFillData(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'fill-array-data (.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, label):
        vm[vx] = vm.array_data[label]["elements"]


class op_IputBoolean(OpCode):
    # iput-boolean v0, p0, Lcom/a;->a:Z

    def __init__(self):
        OpCode.__init__(self, r'^iput-boolean\s*(.+),\s*(.+),\s*(.+)$')

    @staticmethod
    def eval(vm, vx, _, vz):
        vm[vz] = vm[vx]
        vm.result = vm[vz]


class op_IgetBoolean(OpCode):
    # iput-boolean v0, p0, Lcom/a;->a:Z

    def __init__(self):
        OpCode.__init__(self, r'^iget-boolean\s*(.+),\s*(.+),\s*(.+)$')

    @staticmethod
    def eval(vm, vx, _, vz):
        vm[vx] = vm[vz]
        vm.result = vm[vx]


class op_Aget(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^aget[\-a-z]* (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        arr = vm[vy]
        idx = vm[vz]
        vm[vx] = arr[idx]
        vm.result = vm[vx]


class op_AddIntLit(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^add-int/lit\d+ (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, lit):
        vm[vx] = eval("%s + %s" % (vm[vy], lit))

        # import ast
        # # vm[vx]=eval("%s + %s" % (vm[vy], lit))
        # print(vm[vx], ast.literal_eval("%s + %s" % (vm[vy], lit)))


class op_AddInt2Addr(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^add-int/2addr (.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy):
        vm[vx] += int(vm[vy])


class op_MulIntLit(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^mul-int/lit\d+ (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, lit):
        vm[vx] = eval("%s * %s" % (vm[vy], lit))


class op_XorInt2Addr(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^xor-int(/2addr)? (.+),\s*(.+)')

    @staticmethod
    def eval(vm, _, vx, vy):
        # test if vm[vy] is a char instead of an int
        if isinstance(vm[vy], int):
            vm[vx] ^= int(vm[vy])
        else:
            vm[vx] ^= ord(vm[vy])


class op_DivInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^div-int (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        vm[vx] = vm[vy] / vm[vz]


class op_AddInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^add-int (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        vm[vx] = vm[vy] + vm[vz]


class op_SubInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^sub-int (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        vm[vx] = vm[vy] - vm[vz]


class op_MulInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^mul-int (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        vm[vx] = vm[vy] * vm[vz]


class op_RemInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^rem-int (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        vm[vx] = vm[vy] % vm[vz]


class op_AndInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^and-int (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        vm[vx] = vm[vy] & vm[vz]


class op_AndIntLit(OpCode):
    # and-int/lit8 v0, v0, 0x17

    def __init__(self):
        OpCode.__init__(self, r'^and-int/lit\d+ (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, lit):
        vm[vx] = vm[vy] & OpCode.get_int_value(lit)
        vm.result = vm[vx]


class op_NegInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^neg-int (.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy):
        vm[vx] = -vm[vy]


class op_UshrInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^ushr-int (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        vm[vx] = vm[vy] >> vm[vz]


class op_UshrIntLit(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^ushr-int/lit\d+\s*(.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, lit):
        vm[vx] = vm[vy] >> OpCode.get_int_value(lit)


class op_OrInt(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^or-int (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, vz):
        vm[vx] = vm[vy] | vm[vz]


class op_OrIntLit(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^or-int/lit\d+ (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, lit):
        vm[vx] = vm[vy] | OpCode.get_int_value(lit)


class op_GoTo(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^goto(/\d+)? (:.+)')

    @staticmethod
    def eval(vm, _, label):
        vm.goto(label)


class op_NewInstance(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^new-instance (.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, klass):
        vm[vx] = vm.new_instance(klass)


class op_NewArray(OpCode):
    '''new-array vx,vy,type_id

    Generates a new array of type_id type and vy element size and puts the
    reference to the array into vx.
    '''

    def __init__(self):
        OpCode.__init__(self, r'^new-array (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, klass):
        vm[vx] = [""] * vm[vy]


class op_APut(OpCode):
    '''aput vx,vy,vz

    Puts the integer value in vx into an element of an integer array.
    The element is indexed by vz, the array object is referenced by vy.
    '''

    def __init__(self):
        OpCode.__init__(self, r'^aput(-[a-z]+)? (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, _, vx, vy, vz):
        idx = int(vm[vz])
        arr = vm[vy]
        val = vm[vx]
        if len(arr) > idx:
            arr[idx] = val
        elif idx == len(arr):
            arr.append(val)
        vm[vy] = arr


class op_Invoke(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^invoke-([a-z]+) \{(.*)\},\s*(.+)')

    @staticmethod
    def eval(vm, _, args, call):
        args = list(map(str.strip, args.split(',')))
        this = args[0]
        args = args[1:]
        klass, method = call.split(';->')

        vm.invoke(this, klass, method, args)


class op_IntToType(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^int-to-([a-z]+) (.+),\s*(.+)')

    @staticmethod
    def eval(vm, ctype, vx, vy):
        if ctype == 'char':
            vm[vx] = chr(vm[vy] & 0xFF)
        elif ctype == 'byte':
            vm[vx] = vm[vy]
        elif ctype == 'short':
            vm[vx] = vm[vy]
        else:
            raise RuntimeError("op_IntToType: Unsupported type '%s'." % ctype)


class op_SPutObject(OpCode):

    def __init__(self):
        # sput-object v9, Lcom/whatsapp/messaging/a;->z:[Ljava/lang/String;
        # aput-object v6, v8, v7
        OpCode.__init__(self, r'^sput-object+\s(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, staticVariableName):
        vm.variables[staticVariableName] = vm.variables[vx]


class op_SPut(OpCode):

    def __init__(self):
        # const/16 v0, 0xed
        # sput v0, Lcom/a;->g:I
        OpCode.__init__(self, r'^sput\s(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, staticVariableName):
        vm.variables[staticVariableName] = vm.variables[vx]


class op_SGet(OpCode):

    def __init__(self):
        # sget v0, Lcom/a;->g:I
        OpCode.__init__(self, r'^sget+\s(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, staticVariableName):
        vm.variables[vx] = vm.variables[staticVariableName]
        vm.result = vm.variables[vx]


class op_SGetObject(OpCode):

    def __init__(self):
        # sput-object v9, Lcom/whatsapp/messaging/a;->z:[Ljava/lang/String;
        # aput-object v6, v8, v7
        OpCode.__init__(self, r'^sget-object+\s(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, staticVariableName):
        vm.variables[vx] = vm.variables[staticVariableName]
        vm.result = vm.variables[vx]


class op_Return(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^return(-[a-z]*)*\s*(.+)*')

    @staticmethod
    def eval(vm, ctype, vx):
        if (ctype is None and vx is None) or ctype == '-void':
            vm.return_v = None
            vm.stop = True
        elif ctype in ('-wide', '-object') or (ctype is None and vx is not None):
            vm.return_v = vm[vx]
            vm.stop = True

        else:
            raise RuntimeError("Unsupported return type.")


class op_RemIntLit(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^rem-int/lit\d+ (.+),\s*(.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, vy, lit):
        vm[vx] = int(vm[vy]) % OpCode.get_int_value(lit)


class op_PackedSwitch(OpCode):

    def __init__(self):
        OpCode.__init__(self, r'^packed-switch (.+),\s*(.+)')

    @staticmethod
    def eval(vm, vx, table):
        val = vm[vx]
        switch = vm.packed_switches.get(table, {})
        cases = switch.get('cases', [])
        case_idx = val - switch.get('first_value')

        if case_idx >= len(cases) or case_idx < 0:
            return

        case_label = cases[case_idx]

        vm.goto(case_label)
