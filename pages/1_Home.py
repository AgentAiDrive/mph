import streamlit as st
from PIL import Image

st.title("🏠 Welcome to My Parent Helpers")
st.image("MYPARENTHELPERS_512x512.png", width=160)
st.markdown("""
Create personalized AI parenting assistants based on books, styles, or experts.
Start by creating a profile with your parenting approach and your child’s details.
""")

if st.button("🚀 Start Now"):
    st.switch_page("pages/2_Create_Profile.py")
