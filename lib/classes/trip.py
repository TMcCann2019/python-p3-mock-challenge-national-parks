class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.all.append(self)

    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, value):
        from lib.classes.visitor import Visitor
        if isinstance(value, Visitor):
            self._visitor = value
        else:
            raise Exception("Visitor must be an instance of Visitor")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, value):
        from lib.classes.national_park import NationalPark
        if isinstance(value, NationalPark):
            self._national_park = value
        else:
            raise Exception("National Park must be an instance of NationalPark")
        
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value
        else:
            raise Exception("Start date must be a string longer than 7 characters")
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str) and len(value) >= 7:
            self._end_date = value
        else:
            raise Exception("End date must be a string longer than 7 characters")