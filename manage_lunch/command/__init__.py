class BaseCommand():
    @staticmethod
    def add_arguments(parser): raise NotImplemented

    def __init__(self, munch):
        self.munch = munch

    def run(self): raise NotImplemented
