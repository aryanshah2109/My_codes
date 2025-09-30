from fastapi import FastAPI,HTTPException,Query,Path
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel,Field, computed_field
from typing import Annotated, Optional

app = FastAPI()

def load_data():
    with open(r'D:\CODING_CODES\AIML\FastAPI\patients_data.json','r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open(r'D:\CODING_CODES\AIML\FastAPI\patients_data.json','w') as f:
        json.dump(data,f)


class Patient(BaseModel):
    id: str
    name: str = Field(...,title="Name of Patient",description='Enter name of patient',examples=['Aman','Rahul'])
    age: int = Field(...,gt=0,lt=120,title="Age of Patient",description='Enter age of patient')
    gender: str = Field(...,title="Gender of Patient",description='Enter gender of patient',examples=['Male','Female','Others'])
    city: str = Field(...,title="City of Patient",description='Enter city where patient lives',examples=['Mumbai','Delhi','Ahmedabad'])
    height: float = Field(...,gt=0,title="Height of Patient",description='Enter height of patient in meters',examples=[1.23,1.45,1.56])
    weight: float = Field(...,gt=0,title="Weight of Patient",description='Enter weight of patient in kgs',examples=[87,67.3,90.5])

    @computed_field
    @property
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

class PatientUpdate(BaseModel):
    name: Optional[str] =  Field(None, title="Name of Patient",description='Enter name of patient')   
    age: Optional[int] = Field(None, gt=0,lt=120,title="Age of Patient",description='Enter age of patient')
    gender: Optional[str] = Field(None, title="Gender of Patient",)
    city: Optional[str] = Field(None, title="City of Patient",)
    height: Optional[float] = Field(None, gt=0,title="Height of Patient",description='Enter height of patient in meters')
    weight: Optional[float] = Field(None, gt=0,title="Weight of Patient",description='Enter weight of patient in kgs')



@app.get("/")
def home():
    return {'message':'Hello'}

@app.get("/about")
def about():
    return {'message':'Welcome to my application'}

@app.get('/patients')
def patients():
    data = load_data()

    return data

@app.get('/view/{patient_id}')
def getPatientID(patient_id:str=Path(...,description="Id of patient in database",example="P002")):
    data = load_data()

    if patient_id in data.keys():
        return data[patient_id]
    else:
        raise HTTPException(status_code=404,detail="Patient not found")
    

@app.get('/sort')
def sort_patients(sort_by : str = Query(...,description="Sort on the basis of height or weight"), order: str = Query('asc',description="Sort in ascending or descending order")):
    valid_fields = ['height','weight']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=404,detail='Invalid sort_by')

    data = load_data()
    
    sort_order = True if order=='desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=sort_order)

    return sorted_data


@app.post('/create')
def create_patient(patient:Patient):

    # load existing data
    data = load_data()

    # check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')

    # add new patient to database
    data[patient.id] = patient.model_dump(exclude=['id'])

    # save in json file
    save_data(data)

    return JSONResponse(status_code=201,content={'message':'Patient created successfully'})




@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_info: PatientUpdate):
        # load all data
        data = load_data()

        # return 404 if pateint doesn't exist
        if patient_id not in data:
            raise HTTPException(status_code=404,detail='Patient does not exist')
        

        # load patient data from patient id
        patient_current_data = data[patient_id]

        # convert given updated info from pydantic object to dictionary
        patient_updated_data = patient_info.model_dump(exclude_unset=True)


        # update values given in updated info to current info
        for key,value in patient_updated_data.items():
            patient_current_data[key] = value


        # adding id field into new data
        patient_current_data['id'] = patient_id

        # converting new data into Pydantic object to recalculate computed fields
        patient_pydantic_obj = Patient(**patient_current_data)

        # converting Pydantic object back to dictionary excluding id field
        patient_current_data = patient_pydantic_obj.model_dump(exclude={'id'})

        # appending in all data
        data[patient_id] = patient_current_data

        # saving data in file
        save_data(data)

        # returning response regarding successful data updation
        return JSONResponse(status_code=200,content={'message':'Patient data updated successfully'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):
    # load data
    data = load_data()

    # check if patient_id exists or not in data
    if patient_id not in data.keys():
        raise HTTPException(status_code=404,detail='Patient does not exist in database')
    
    # select key from data
    del data[patient_id]

    # save data
    save_data(data)

    return JSONResponse(status_code=200,content='Successfully deleted record')
