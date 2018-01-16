from manage_lunch.role.plugin import ManageLunchPlugin

class ChooseLunchPlugin(ManageLunchPlugin):
    def pick_lunch(self): raise NotImplementedError
    def set_lunch(self, lunch): self.munch.lunch.append(lunch)
