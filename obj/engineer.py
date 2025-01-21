# class definition for an Engineer

class Engineer(object):
    counter = 0
    name=""
    address=""
    def __init__(self, full_name:str='', address:str=''):
        self.name = full_name
        self.address = address
        self.counter += 1


    @property
    def name(self):
        return self.name


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
        return self.address


    @address.setter
    def address(self, address:str):
        self.address = address.upper()
