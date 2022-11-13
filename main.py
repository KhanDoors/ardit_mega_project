import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo1.png")

with col2:
    st.title("Capt. Khan")
    content = """
    Hi, I am captain! I am a Python programmer, teacher, and founder of Khandoor. I graduated from the University of StonyBrook in N.Y. with a focus on using Python for remote sensing.
I have worked with companies from various countries, such as the Khandoor.
    """
    st.info(content)
