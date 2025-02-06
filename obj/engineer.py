# class definition for an Engineer
from obj import job

class Engineer(object):
    counter = 0
    name=""
    address=""
    def __init__(self, full_name:str='', address:str=''):
        self.name = full_name
        self.address = address
        self.counter += 1
        self.jobs = []


    @property
    def name(self):
        return self._name


    @name.setter
    def name(self, name:str):
        self._name = name


    @property
    def first_name(self):
        return self.name.split(" ")[0]


    @property
    def last_name(self):
        if len(self.name.split(" ")) < 2:
            return ""
        else:
            return " ".join(self.name.split(" ")[1:])


    @property
    def address(self):
        return self._address


    @address.setter
    def address(self, address:str):
        self._address = address.upper()

    
    def add_job(self, job:job.Job):
        self.jobs.append(job)

    
    def get_all_jobs(self):
        return self.jobs