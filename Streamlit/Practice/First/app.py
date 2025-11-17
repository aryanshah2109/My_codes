import streamlit as st
import os

st.write("Hello world")

st.title("This is a title")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.markdown("This is a markdown")
st.markdown("This is an italic _markdown_")
st.markdown("This is an bold __markdown__")

code_demo = """
def greet(name):
    return f"Hello {name}"
"""

st.code(code_demo,language='python')

st.divider()

# adding an image

st.image(os.path.join(os.getcwd(),""))