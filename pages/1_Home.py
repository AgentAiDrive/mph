import streamlit as st
import os
import json
from app_utils import apply_mobile_style

# --- Global mobile “phone” container + theme + centered cards CSS ---
apply_mobile_style()
st.markdown("""
    <style>
    .dashboard {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 16px;
      width: 100%;
      padding: 10px 0;
    }

    /* card base with centered contents */
    .card {
      border-radius: 16px;
      padding: 10px;
      color: white;
      box-shadow: 0 4px 10px rgba(0,0,0,0.15);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }
    /* subtle bright palette */
    .blue   { background-color: #64B5F6; }  /* sky blue */
    .red    { background-color: #E57373; }  /* soft red */
    .green  { background-color: #81C784; }  /* mint green */
    .purple { background-color: #BA68C8; }  /* lavender */

    .card h2 {
      margin: 0;
      font-size: 24px;
    }
    .card small {
      display: block;
      margin-bottom: 6px;
      font-size: 18px;
      opacity: 0.9;
    }
    .card a {
      display: inline-block;
      background-color: rgba(255,255,255,0.15);
      border-radius: 20px;
      padding: 8px;
      font-size: 16px;
      color: black;
      text-decoration: none;
      transition: background-color 0.2s ease;
      margin-top: 8px;
    }
    .card a:hover {
      background-color: rgba(255,255,255,0.25);
    }
    </style>
""", unsafe_allow_html=True)

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
