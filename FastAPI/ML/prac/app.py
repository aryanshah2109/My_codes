import numpy as np
from fastapi import FastAPI
import pickle as pkl
from typing import Literal, Annotated, Optional
from pydantic import BaseModel, Field, computed_field
import pandas as pd
from fastapi.responses import JSONResponse

# import model
with open(r'D:\CODING_CODES\AIML\FastAPI\ML\prac\linear_regression_model.pkl','r') as f:
    model = pkl.load(f)


class UserInput(BaseModel):
    experience: Annotated[Optional[float],Field(...,title='Enter experience in years',description='How much experience do you have in years',examples=[5.9,30.5])]
    education_score: Annotated[Optional[float],Field(...,title='Enter education score',description='What is your education score',examples=[15.4,31.9])]
    certifications: Annotated[Optional[float],Field(...,title='Enter number of certifications',description='How many',examples=[3,6])]


app = FastAPI()

@app.post('/predict')
def predict_function(data: UserInput):

    data = pd.DataFrame([data])

    prediction = model.predict(data)[0]

    return JSONResponse(content=f'Predicted salary is: {prediction}',status_code=200)
