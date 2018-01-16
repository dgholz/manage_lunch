from manage_lunch.role import ManageLunchRole

class ManageLunchPlugin(ManageLunchRole):
    def __init__(self, munch):
        self.munch = munch

    def register(self):
        self.munch.plugins.append(self)
