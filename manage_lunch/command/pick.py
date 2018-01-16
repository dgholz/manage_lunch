'''Pick a lunch from the allowed options'''
from manage_lunch.command import BaseCommand
from manage_lunch.plugin.lunch_places import LunchPlaces

class PickCommand(BaseCommand):
    def __init__(self, munch, allowed):
        super().__init__(munch)
        self.allowed = allowed
        self.plugin = LunchPlaces(munch, *allowed)

    @staticmethod
    def add_arguments(parser):
        parser.add_argument('allowed', nargs='*')
        return parser

    def run(self):
        self.plugin.register()
        print(self.munch.choose_a_place_to_eat())
