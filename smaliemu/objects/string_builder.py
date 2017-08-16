class StringBuilder:

    @staticmethod
    def name():
        return 'java.lang.StringBuilder'

    @staticmethod
    def methods():
        return {
            'new-instance': StringBuilder.new_instance,
            '<init>()V': StringBuilder.init,
            '<init>(Ljava/lang/String;)V': StringBuilder.init_from_string,
            'append(Ljava/lang/String;)Ljava/lang/StringBuilder;': StringBuilder.append,
            'append(C)Ljava/lang/StringBuilder;': StringBuilder.append,
            'insert(ILjava/lang/String;)Ljava/lang/StringBuilder;': StringBuilder.insert,
            'toString()Ljava/lang/String;': StringBuilder.tostring
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
