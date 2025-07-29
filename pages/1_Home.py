import streamlit as st
import os
import json
from app_utils import apply_phone_style

st.set_page_config(page_title="My Parent Helpers", page_icon="👨‍👩‍👧‍👦")

# --- Global mobile “phone” container + theme + centered cards CSS ---
apply_phone_style()

# --- Logo + Title ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("MYPARENTHELPERS_512x512.png", width=50)
with col2:
    st.markdown(
        '<h3 style="margin:10px; font-size:20px;">My Parent Helpers</h3>',
        unsafe_allow_html=True)
st.markdown("---")
# --- Main page links as a 2×2 card grid ---
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
