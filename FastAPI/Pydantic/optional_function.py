from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Person(BaseModel):
    name: Annotated[str,Field(max_length=50,title="Name of Patient",description="Give the name of the patient",examples=['Nitesh','Arjun'])]
    age: int = Field(gt=0,strict=True)
    salary: Optional[float] = None
    married: bool = False
    email: EmailStr
    linkedin : AnyUrl



def insert_person(person:Person):
    print(person.name)
    print(person.age)
    print(person.salary)
    print(person.married)
    print(person.email)

person1_info = {
    'name':'Aman',
    'age':24,
    'married':True,
    'email':'aman12@gmail.com',
    'linkedin':'https://linkedin.com/aman12'
}


person1 = Person(**person1_info)
insert_person(person1)