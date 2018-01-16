import random

from manage_lunch.role.choose_lunch import ChooseLunchPlugin

class RandomPicker(ChooseLunchPlugin):
    def pick_lunch(self):
        self.set_lunch(random.choice(self.munch.available))
