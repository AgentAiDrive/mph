import streamlit as st
from PIL import Image
import os
import json
from app_utils import apply_phone_style
from app_utils import get_openai_key

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

# --- Global mobile “phone” container + theme + centered cards CSS ---
apply_phone_style()


st.markdown('<div class="dashboard">', unsafe_allow_html=True)
pages = [
    ("red",    "👤  PROFILES", "Create a new pAIrenting agent profile", "/Create_Profile", "NEW"),
    ("blue",   "💬  CHAT",     "Chat with your pAIrent agent",           "/Chat_Helper",   "CHAT"),
    ("green",  "📁  SAVED",    "View saved chats",                       "/Saved_Items",   "VIEW"),
    ("purple", "🆘  SUPPORT",  "Get help & resources",                  "/Support",       "HELP"),
]

for color, title, subtitle, link, btn in pages:
    st.markdown(f"""
      <div class="card {color}">
        <h2>{title}</h2>
        <small>{subtitle}</small>
        <a href="{link}">{btn}</a>
      </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
