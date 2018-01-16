from manage_lunch.role.gather_lunch_plugin import GatherLunchPlugin

class LunchPlaces(GatherLunchPlugin):
    def __init__(self, munch, places):
        super().__init__(munch)
        self.places = places


    def make_suggestions(self):
        for place in self.places:
            self.add_suggestion(place)
