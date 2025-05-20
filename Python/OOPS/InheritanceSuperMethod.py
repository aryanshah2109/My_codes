# To access methods of parent class, we use super().method

class Person:
    gender = "Male"
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    @staticmethod
    def hello():
        print("Hello world")
    
class Student(Person):
    def __init__(self, eRollNo, grade, name, age, height, weight):
        self.eRollNo = eRollNo
        self.grade = grade
        super().__init__(name,age,height,weight)
        super().hello()
        print(super().gender)

s1 = Student(10,99,"Aryan",32,190,100)
print(s1.eRollNo,s1.grade,s1.name,s1.age,s1.height,s1.weight)



