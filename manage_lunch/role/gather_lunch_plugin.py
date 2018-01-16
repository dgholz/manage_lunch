from manage_lunch.role.plugin import ManageLunchPlugin

class GatherLunchPlugin(ManageLunchPlugin):
    def make_suggestions(self): raise NotImplementedError
    def add_suggestion(self, place): self.munch.available.append(place)
