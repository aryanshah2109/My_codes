from pydantic import BaseModel, computed_field
from typing import List,Dict, Optional

class Patient(BaseModel):
    name: str
    age: int
    height: float
    weight : float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculate_bmi(self)->float:
        bmi = round(self.weight/(self.height**2))
        return bmi


def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(f'BMI: {patient.calculate_bmi}')
    print(patient.contact_details)

patient1_info = {'name':'Aryan','age':20,'height':1.80,'weight':87.3,'married':False,'allergies':['pollen','dust'],'contact_details':{'phone_num':'720351512','email':'aryan151@gmail.com'}}
patient2_info = {'name':'Jayani','age':20,'height':1.76,'weight':77.3,'married':False,'contact_details':{'phone_num':'982551512','email':'jayani1127@gmail.com'}}

patient1 = Patient(**patient1_info)
insert_patient_data(patient1)

patient2 = Patient(**patient2_info)
insert_patient_data(patient2)