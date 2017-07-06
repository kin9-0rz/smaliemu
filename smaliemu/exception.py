

class UnsupportedOpcodeError(RuntimeError):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message
