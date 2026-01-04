import streamlit as st
import datetime
import json

import os

os.makedirs("Form_data", exist_ok=True)

file_path = "Form_data/data.json"

# Load existing data
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        try:
            existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []
else:
    existing_data = []

st.title("Form Tutorial")
st.divider()


with st.form("my_form"):

    st.header("Registration Form")
    
    col1, col2 = st.columns(2)

    with col1:
        fname = st.text_input("First name", placeholder="Enter first name")
    
    with col2:
        lname = st.text_input("Last name", placeholder="Enter last name")
    
    marks = st.number_input("Marks: ", min_value=0, max_value=150)

    dob = st.date_input("Birthdate", datetime.date(2018,1,1), min_value = datetime.date(1500,1,1), max_value=datetime.date.today())

    gender = st.radio(
        "Gender: ",
        ("Male","Female","Others")
    )


    address = st.text_area("Address", placeholder="Enter your address")

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
       
    if not fname:
        st.error("First name is required") 

    elif not lname:
        st.error("Last name is required")
    
    elif not gender:
        st.error("Gender is required")

    elif not marks:
        st.error("Marks are required")

    elif marks < 1 or marks > 150:
        st.error("Marks must be between 1 to 150 only")

    else:
        st.success("Form submitted successfully")

    data = {
        "fname": f"{fname}",
        "lname": f"{lname}",
        "gender": gender,
        "dob": dob.isoformat(),
        "address": f"{address}"
    }

    existing_data.append(data)

    with open("Form_data/data.json","w") as f:
        json.dump(existing_data, f, indent=3)    
