class BaseCommand():
    @staticmethod
    def add_arguments(parser): raise NotImplemented

    def __init__(self, manage_lunch):
        self.manage_lunch = manage_lunch

    def run(self): raise NotImplemented
