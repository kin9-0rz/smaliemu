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
        vm.return_v = vm[args[0]]
        vm[this] = vm[args[0]]

    @staticmethod
    def append(vm, this, args):
        vm[this] += vm[args[0]]
        vm.return_v = vm[this]

    @staticmethod
    def tostring(vm, this, args):
        vm.return_v = vm[this]
