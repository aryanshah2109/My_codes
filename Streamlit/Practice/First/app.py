import streamlit as st
import os

st.write("Hello world")

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.markdown("This is a markdown")
st.markdown("This is an italic _markdown_")
st.markdown("This is a bold __markdown__")



code_demo = """
def greet(name):
    return f"Hello {name}"
"""

st.code(code_demo,language='python')

st.divider()

# Buttons
button1 = st.button("Click me!")
if button1:
    st.write("You clicked the button!")

st.divider()

# Checkboxes
like = st.checkbox("Do you like this app?")
submit_btn = st.button("Submit")

if like and submit_btn:
    st.write("Thank you!")
elif submit_btn:
    st.write("Please leave a review below to help us improve!")

st.divider()

# Radio buttons
animal = st.radio("What animal is your favourite?", ("Lion","Tiger","Rabbit","None"))
submit_animal = st.button("Submit Animal")

if submit_animal:
    if animal != "None":
        st.write(animal)
    else:
        inp = st.text_input("Enter your favourite animal")
        if inp != "":
            st.write(inp)

st.divider()

# Dropbox
food = st.selectbox("What is your favourite food?", ("--Select--","Pizza","Burger","Nachos","Noodles","Sushi"))
submit_food = st.button("Submit Food")

if food and submit_food:
    if food != "--Select--":
        st.write(food)
    else:
        st.write("Please select a food!")

st.divider()

# Multiple select dropbox
subject = st.multiselect("Select Subjects", ("English","Math","Science","PE"))
submit_subject = st.button("Submit Subject")


if subject and submit_subject:
    for sub in subject:
        st.write(sub)

st.divider()

# Numerical Slider 
age = st.slider("Enter Age: ", min_value=1, max_value=150, value=20)

if st.button("Submit Age"):
    st.write(f"Your age: {age}")

st.divider()

# Text input
name = st.text_input("Enter name: ", value="Joe Doe")

if st.button("Submit Name"):
    st.write(f"Your name: {name}")

st.divider()

# Numerical input
marks = st.number_input("Enter marks: ", value=50)

if st.button("Submit Marks"):
    st.write(f"Your marks: {marks}")

st.divider()

# Text Area

txt = st.text_area("Enter blog: ", value = '''With WordPress 6.9 you can work together, create faster, and build with more control. Leave notes right on your blocks, drag and drop with ease, and use the command palette anywhere, including the admin, to stay in flow. From stretchy text that fits perfectly to new blocks like Accordion, MathML, and Time to Read, every detail is built to make collaboration and creation smoother.''', height=250)

if st.button("Submit text"):
    st.write(f"Text length: {len(txt)} characters")
