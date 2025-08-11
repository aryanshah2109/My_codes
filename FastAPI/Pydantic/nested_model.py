from pydantic import BaseModel,Field
from typing import List, Dict

class Address(BaseModel):
    city: str
    state: str
    pincode: str

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    address: Address

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.gender)
    print(patient.address)
    print(patient.address.city)
    print(patient.address.state)
    print(patient.address.pincode) 

address_info = {
    'city':'Ahmedabad',
    'state':'Gujarat',
    'pincode':'382481'
}
address1 = Address(**address_info)

patient_info = {
    'name':'Aryan',
    'age':34,
    'gender': 'Male',
    'address':address1
}
patient1 = Patient(**patient_info)

insert_patient_data(patient1)


