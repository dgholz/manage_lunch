from random import choice

from manage_lunch.command import BaseCommand

class PickCommand(BaseCommand):
    def __init__(self, manage_lunch, *allowed):
        super(__class__)(self, manage_lunch)
        self.allowed = allowed

    @staticmethod
    def add_arguments(parser):
        parser.add_argument('allowed', nargs='*')
        return parser

    def run(self):
        print(choice(self.allowed))
