# Used to change class properties permanently

class Person:
    name = "No Name"    

    @classmethod
    def changeName(cls,newName):
        cls.name = newName
    
    # This also means the same
    # def changeName(self,newName):
    #     self.__class__.name = newName

a = Person()
b = Person()
print(a.name)
print(b.name)
a.changeName("Aryan")
print(a.name)
print(b.name)