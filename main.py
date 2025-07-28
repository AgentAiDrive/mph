import streamlit as st
from PIL import Image
from app_utils import load_api_key

st.set_page_config(page_title="My Parent Helpers", page_icon="👨‍👩‍👧‍👦", layout="centered")

logo = Image.open("MYPARENTHELPERS_512x512.png")

with st.sidebar:
    st.image(logo, width=100)
    st.title("📚 My Parent Helpers")
    st.page_link("pages/1_Home.py", label="Home", icon="🏠")
    st.page_link("pages/2_Create_Profile.py", label="Create Profile", icon="🧬")
    st.page_link("pages/3_Chat_Helper.py", label="Parent Chat", icon="💬")
    st.page_link("pages/4_Saved_Items.py", label="Saved Files", icon="📁")
    st.page_link("pages/5_Support.py", label="Support", icon="🆘")

key = load_api_key(use_sidebar=False)
if not key:
    st.error("OpenAI API key required for chat features.")
