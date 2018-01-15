class ManageLunchPlugin:
    def __init__(self, munch):
        self.munch = munch

    def register(self):
        self.munch.plugins.append(self)
