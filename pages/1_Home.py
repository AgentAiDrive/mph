import streamlit as st
import os
import json

# --- Global mobile “phone” container + theme ---
st.markdown("""
    <style>
    /* page background */
    body {
      background: linear-gradient(135deg, #2fe273 0%, #09742a 100%) !important;
      min-height: 100vh;
    }
    /* the “phone” wrapper */
    .stApp {
      background: linear-gradient(335deg, #2fe273 0%, #09742a 100%) !important;
      border-radius: 32px;
      max-width: 400px;
      min-height: 100vh;
      height: 100vh;
      overflow-y: auto;
      margin: 32px auto;
      box-shadow: 0 8px 32px rgba(60,60,60,0.25),
                  0 1.5px 8px rgba(30,90,40,0.06);
      border: 3px solid #ffffff;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 10px;
    }

    /* two-column grid helper */
    .dashboard {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        width: 100%;
        padding: 10px 0;
    }

    /* card base */
    .card {
        border-radius: 16px;
        padding: 10px 10px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    /* card colors */
    .blue   { background-color: #64B5F6; }  /* sky blue */
    .red    { background-color: #E57373; }  /* soft red */
    .green  { background-color: #81C784; }  /* mint green */
    .purple { background-color: #BA68C8; }  /* lavender */

    .card h2 {
        margin: 0 0 0px 0px;
        text-align: center;
        text-decoration: none;
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
        padding: 8px 8px;
        font-size: 16px;
        color: black;
        text-decoration: none;
        transition: background-color 0.2s ease;
    }
    .card a:hover {
        background-color: rgba(255,255,255,0.25);
    }
 """, unsafe_allow_html=True)

# --- Logo + Title ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("MYPARENTHELPERS_512x512.png", width=80)
with col2:
    st.markdown(
     '<h3 style="margin:0; font-size:20px;">My Parent Helpers</h3>',
   unsafe_allow_html=True)
 st.markdown("---")

# --- Main page links as a 2×2 card grid ---
st.markdown('<div class="dashboard">', unsafe_allow_html=True)

pages = [
    ("red",    "PROFILES", "Create a new pAIrenting agent profile", "/Create_Profile", "NEW"),
    ("blue",   "CHAT",    "Chat with your pAIrent agent",     "/Chat_Helper",   "CHAT"),
    ("green",  "SAVED",    "View saved chats",           "/Saved_Items",   "VIEW"),
    ("purple", "SUPPORT",        "Get help & resources",        "/Support",       "HELP"),
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
