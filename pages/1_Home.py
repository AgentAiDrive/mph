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
        padding: 24px 16px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    /* card colors */
    .red    { background-color: #f94144; }
    .blue   { background-color: #577590; }
    .green  { background-color: #43aa8b; }
    .purple { background-color: #6a4c93; }

    .card h2 {
        margin: 0 0 0px 0px;
        text-decoration: overline underline;
        font-size: 24px;
    }
    .card small {
        display: block;
        margin-bottom: 6px;
        font-size: 20px;
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

    /* static top nav */
    .top-nav {
        width: 100%;
        display: flex;
        justify-content: space-around;
        background: #43aa8b;
        padding: 12px 0;
        border-bottom: 1px solid #eee;
        margin-bottom: 16px;
    }
    .nav-link {
        font-size: 16px;
        text-decoration: none;
        color: #ffffff;
        padding: 8px 12px;
        border-radius: 8px;
        transition: background-color 0.2s ease;
    }
    .nav-link:hover {
        background-color: rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)


# --- Top navigation ---
st.markdown("""
  <div class="top-nav">
    <a href="Home" class="nav-link">HOME</a>
    <a href="Chat_Helper"   class="nav-link">CHAT</a>
    <a href="Saved_Items"   class="nav-link">SAVED</a>
  </div>
""", unsafe_allow_html=True)

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
