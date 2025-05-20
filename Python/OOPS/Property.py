# @property -> getter method
# @name.setter -> setter method
class Person:
    namePerson = ""
    def __init__(self,phy,maths,chem):
        self.phy = phy
        self.maths = maths
        self.chem = chem
    
    @property
    def name(self):
        return self.namePerson
    
    @name.setter
    def name(self,name):
        if name:    # checks if name is added as argument in function call
            self.namePerson = name
        else:
            raise TypeError("Name cant be empty")

a = Person(39,98,46)
a.name = "Aryan"
print(a.name)