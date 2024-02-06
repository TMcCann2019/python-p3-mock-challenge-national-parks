class Visitor:

    all_visitors = []

    def __init__(self, name):
        self.name = name
        self.all_visitors.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 0 < len(value) < 16:
            self._name = value
        else:
            raise Exception("Name must be a string greater than 0 and less than 16")
        
    def trips(self):
        from lib.classes.trip import Trip
        return [trip for trip in Trip.all if trip.visitor == self]
        pass
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
        pass
    
    # def total_visits_at_park(self, park):
    #     total_visits = 0
    #     for trip in self.trips():
    #         if trip.national_park == park:
    #             total_visits += 1
    #     return total_visits
    #     pass