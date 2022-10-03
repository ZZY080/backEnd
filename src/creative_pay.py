from module.singleton_type import SingletonType


class CreativePay(metaclass=SingletonType):
    def __init__(self):
        super(CreativePay, self).__init__()

    def start(self):
        pass

    def stop(self):
        pass
