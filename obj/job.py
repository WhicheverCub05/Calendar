# class definition for a job

class Job:
    _counter = 0

    def __init__(self):
        self.description = ""
        self.duration = ""
        self.location = ""
        self.id = ""
        self._counter += 1

    
    @property
    def location(self):
        return self._location
    
    
    @location.setter
    def location(self, location:str):
        self._location = location.upper()
        
    
    @property
    def duration(self):
        return self._duration


    @duration.setter
    def duration(self, duration):
        self._duration = duration

    
    @property
    def description(self):
        return self._description
    

    @description.setter
    def description(self, description):
        self._description = description
    

    @property
    def id(self):
        return self._id


    @id.setter
    def id(self, id):
        self._id = id


    @property
    def counter(self):
        return self._counter