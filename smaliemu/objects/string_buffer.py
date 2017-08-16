class StringBuffer:

    @staticmethod
    def name():
        return 'java.lang.StringBuffer'

    @staticmethod
    def methods():
        return {
            'new-instance': StringBuffer.new_instance,
            '<init>()V': StringBuffer.init,
            '<init>(Ljava/lang/String;)V': StringBuffer.init_from_string,
            'append(Ljava/lang/String;)Ljava/lang/StringBuffer;': StringBuffer.append,
            'append(C)Ljava/lang/StringBuffer;': StringBuffer.append,
            'insert(ILjava/lang/String;)Ljava/lang/StringBuffer;': StringBuffer.insert,
            'toString()Ljava/lang/String;': StringBuffer.tostring
        }

    @staticmethod
    def new_instance():
        return ""

    @staticmethod
    def init(vm, this, args):
        pass

    @staticmethod
    def init_from_string(vm, this, args):
        vm.result = vm[args[0]]
        vm[this] = vm.result

    @staticmethod
    def append(vm, this, args):
        vm[this] += vm[args[0]]
        vm.result = vm[this]

    @staticmethod
    def insert(vm, this, args):
        original = vm[this]
        pos = vm[args[0]]
        new = vm[args[1]]
        vm[this] = original[:pos] + new + original[pos:]
        vm.result = vm[this]

    @staticmethod
    def tostring(vm, this, args):
        vm.result = vm[this]
