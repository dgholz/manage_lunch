'''Pick a lunch from the allowed options'''
from random import choice

from manage_lunch.command import BaseCommand

class PickCommand(BaseCommand):
    def __init__(self, munch, allowed):
        super().__init__(munch)
        self.allowed = allowed

    @staticmethod
    def add_arguments(parser):
        parser.add_argument('allowed', nargs='*')
        return parser

    def run(self):
        print(choice(self.allowed))
