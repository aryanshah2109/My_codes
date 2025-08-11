from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Person(BaseModel):
    name: str
    age: int = Field(gt=0,strict=True)
    salary: Optional[float] = None
    married: bool = False
    email: EmailStr
    linkedin : AnyUrl

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdf.com','icici.com','gmail.com']
        domain_name = value.split('@')[1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value
    
    @field_validator('name')
    @classmethod
    def name_lower(cls,value):
        return value.lower()
        



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