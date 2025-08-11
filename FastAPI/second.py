from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()
def load_data():
    with open(r'patients_data.json','r') as f:
        data = json.load(f)
    return data

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


