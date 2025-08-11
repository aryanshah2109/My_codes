from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator
from typing import List, Dict, Optional, Annotated

class Person(BaseModel):
    name: str
    age: int = Field(gt=0,strict=True)
    salary: Optional[float] = None
    married: bool = False
    email: EmailStr
    linkedin : AnyUrl
    contact_details : Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains = ['hdf.com','icici.com','gmail.com']
        domain_name = value.split('@')[1]
        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        return value
    
    @model_validator(mode='after')
    def validate_emergency_num(cls,model):
        if model.age>60 and 'emergency_num' not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency number")
        else:
            return model

        



def insert_person(person:Person):
    print(person.name)
    print(person.age)
    print(person.salary)
    print(person.married)
    print(person.email)

person1_info = {
    'name':'Aman',
    'age':90,
    'married':True,
    'email':'aman12@gmail.com',
    'linkedin':'https://linkedin.com/aman12',
    'contact_details':{'phone':'9150385093','emergency_num':'9352386548'}
}


person1 = Person(**person1_info)
insert_person(person1)