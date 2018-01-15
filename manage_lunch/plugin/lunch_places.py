from manage_lunch.role.gather_lunch_plugin import GatherLunchPlugin

class LunchPlaces(GatherLunchPlugin):
    @classmethod
    def multivalue_aliases(cls):
        return { 'place': 'places' }

    def __init__(self, munch, *rest, **kwargs):
        super().__init__(munch)
        places = kwargs.pop('places', [])
        places.extend(rest)
        self.places = places


    def make_suggestions(self):
        for place in self.places:
            self.add_suggestion(place)
