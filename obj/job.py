# class definition for a job

class Job:
    counter = 0

    def __init__(self):
        self.location = ""
        self.task = ""
        self.counter += 1

    
    @property
    def location(self):
        return self.location
    
    
    @location.setter
    def location(self, location:str):
        self.location = location.upper()
        
    
    @property
    def task(self):
        return self.task


    @task.setter
    def task(self, task):
        self.task = task
    