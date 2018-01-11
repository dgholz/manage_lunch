'''Buy Me Lunch'''
import random

class ManageLunch():
    def __init__(self): pass

    def lunch_suggestions(self, places):
        self.available = places

    def choose_a_place_to_eat(self):
        return random.choice(self.available)
