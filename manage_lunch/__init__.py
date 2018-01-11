'''Buy Me Lunch'''
import random

class ManageLunch():
    def __init__(self):
        self.plugins = []

    def lunch_suggestions(self, places):
        self.available = places

    def choose_a_place_to_eat(self):
        for plugin in self.plugins:
            plugin.pick_lunch()
        return self.lunch
