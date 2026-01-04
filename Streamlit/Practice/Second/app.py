import streamlit as st

st.title("Layout")

# Nav bar
st.sidebar.header("Options")

st.sidebar.image("D://CODING_CODES/AIML/Streamlit/Practice/Second/static/hqdefault.jpg", caption="Image")

default = "Enter Long Text"

text = st.sidebar.text_area("Enter text: ", value=default)

if st.sidebar.button("Submit"):
    col1, col2 = st.columns(2)

    with col1:
        st.header("Original Text")
        st.write(text)

    with col2:
        st.header("Cleaned Text")
        st.write(text)

    