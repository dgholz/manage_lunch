import random

from manage_lunch.role.plugin import ManageLunchPlugin

class RandomPicker(ManageLunchPlugin):
    def pick_lunch(self):
        self.munch.lunch = random.choice(self.munch.available)
