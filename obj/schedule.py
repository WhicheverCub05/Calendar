# class definition for a Schedule
from .engineer import Engineer
from .job import Job

class Schedule:

    def __init__(self, engineer:Engineer):
        engineer = None
        jobs = []


    @property
    def engineer(self) -> Engineer:
        return self.engineer


    @engineer.setter
    def engineer(self, engineer:Engineer):
        self.engineer = engineer


    @property
    def jobs(self) -> list[Job]:
        return self.jobs


    @jobs.setter
    def jobs(self, jobs:list[Job]):
        self.jobs = jobs