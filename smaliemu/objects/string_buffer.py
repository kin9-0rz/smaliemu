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
        vm.return_v = vm[args[0]]
        vm[this] = vm[args[0]]

    @staticmethod
    def append(vm, this, args):
        vm[this] += vm[args[0]]
        vm.return_v = vm[this]

    @staticmethod
    def tostring(vm, this, args):
        vm.return_v = vm[this]
