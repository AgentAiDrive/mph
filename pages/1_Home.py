import streamlit as st
import os
import json
from app_utils import apply_phone_style

st.set_page_config(page_title="My Parent Helpers", page_icon="👨‍👩‍👧‍👦", initial_sidebar_state="collapsed")

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
