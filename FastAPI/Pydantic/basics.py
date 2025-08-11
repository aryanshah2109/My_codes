from pydantic import BaseModel
from typing import List,Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    weight : float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

patient1_info = {'name':'Aryan','age':20,'weight':87.3,'married':False,'allergies':['pollen','dust'],'contact_details':{'phone_num':'720351512','email':'aryan151@gmail.com'}}
patient2_info = {'name':'Jayani','age':20,'weight':77.3,'married':False,'contact_details':{'phone_num':'982551512','email':'jayani1127@gmail.com'}}

patient1 = Patient(**patient1_info)
insert_patient_data(patient1)

patient2 = Patient(**patient2_info)
insert_patient_data(patient2)