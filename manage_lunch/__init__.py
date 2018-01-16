'''Buy Me Lunch'''
import random

class ManageLunch():
    def __init__(self):
        self.plugins = []
        self.available = []
        self.lunch = []

    def plugins_with(self, role_name):
        return [plugin for plugin in self.plugins if plugin.does(role_name)]

    def choose_a_place_to_eat(self):
        for plugin in self.plugins_with('GatherLunchPlugin'):
            plugin.make_suggestions()
        for plugin in self.plugins_with('ChooseLunchPlugin'):
            plugin.pick_lunch()
        return self.lunch[0]
