import random

from manage_lunch.role.plugin import ManageLunchPlugin

class RandomPicker(ManageLunchPlugin):
    def __init__(self, munch):
        self.munch = munch

    def pick_lunch(self):
        self.munch.lunch = random.choice(self.munch.available)
