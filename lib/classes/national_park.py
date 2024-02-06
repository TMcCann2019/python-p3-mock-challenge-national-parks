from lib.classes.trip import Trip

class NationalPark:
    all_parks = []

    def __init__(self, name):
        self.name = name
        self.all_parks.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) >= 3 and not hasattr(self, '_name'):
            self._name = value
        else:
            raise Exception("Name must be a string longer than 3 characters")
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
        pass
    
    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
        pass
    
    def total_visits(self):
        return len(self.trips())
        pass
    
    def best_visitor(self):
        max_visitor = None
        max_visits = 0
        for visitor in self.visitors():
            v_visits = len([ trip for trip in self.trips() if trip.visitor == visitor])
            if v_visits > max_visits:
                max_visits = v_visits
                max_visitor = visitor
        return max_visitor
        pass