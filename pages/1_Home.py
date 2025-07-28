import streamlit as st
import os
import json

# --- Global mobile-friendly styling + app CSS ---
st.markdown("""
    <style>
    /* Mobile “phone” container */
    body {
      background: linear-gradient(135deg, #2fe273 0%, #09742a 100%) !important;
      min-height: 100vh;
    }
    .stApp {
      background: linear-gradient(335deg, #2fe273 0%, #09742a 100%) !important;
      border-radius: 32px;
      max-width: 400px;
      min-height: 100vh;
      height: 100vh;
      overflow-y: auto;
      margin: 32px auto;
      box-shadow: 0 8px 32px rgba(60,60,60,0.25), 0 1.5px 8px rgba(30,90,40,0.06);
      border: 3px solid #ffffff;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 10px;
    }

    /* Grid for cards */
    .dashboard {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        width: 100%;
        padding: 10px 0;
    }
    /* Individual card styling */
    .card {
        border-radius: 16px;
        padding: 24px 16px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        position: relative;
    }
    .red    { background-color: #f94144; }
    .blue   { background-color: #577590; }
    .green  { background-color: #43aa8b; }
    .purple { background-color: #6a4c93; }

    .card h2 {
        margin: 0 0 8px;
        font-size: 22px;
    }
    .card small {
        display: block;
        margin-bottom: 16px;
        font-size: 14px;
        opacity: 0.9;
    }
    .card a {
        display: inline-block;
        background-color: rgba(255,255,255,0.15);
        border: none;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 14px;
        color: white;
        text-decoration: none;
        transition: background-color 0.2s ease;
    }
    .card a:hover {
        background-color: rgba(255,255,255,0.25);
    }

    /* Static top nav bar */
    .top-nav {
        width: 100%;
        display: flex;
        justify-content: space-around;
        background: #ffffff;
        padding: 12px 0;
        border-bottom: 1px solid #eee;
        margin-bottom: 16px;
    }
    .nav-link {
        font-size: 16px;
        text-decoration: none;
        color: #333;
        padding: 8px 12px;
        border-radius: 8px;
        transition: background-color 0.2s ease;
    }
    .nav-link:hover {
        background-color: rgba(0,0,0,0.05);
    }
    </style>
""", unsafe_allow_html=True)


# --- Top Navigation ---
st.markdown("""
    <div class="top-nav">
      <a href="?page=2_Create_Profile" class="nav-link">Home</a>
      <a href="?page=3_Chat_Helper"   class="nav-link">Chat</a>
      <a href="?page=4_Saved_Items"   class="nav-link">Saved</a>
    </div>
""", unsafe_allow_html=True)


# --- Dashboard Cards ---
st.markdown('<div class="dashboard">', unsafe_allow_html=True)

cards = [
    ("red",    "🧬 Create Profile", "Define a new parenting profile", "/?page=2_Create_Profile", "Go"),
    ("blue",   "💬 Parent Chat",    "Chat with your AI agent",    "/?page=3_Chat_Helper",   "Chat"),
    ("green",  "📁 Saved Items",    "Browse your saved data",     "/?page=4_Saved_Items",   "View"),
    ("purple", "🆘 Support",        "Get help and resources",     "/?page=5_Support",       "Help"),
]

for color, title, subtitle, link, btn in cards:
    st.markdown(f"""
        <div class="card {color}">
            <h2>{title}</h2>
            <small>{subtitle}</small>
            <a href="{link}" class="nav-link">{btn}</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
```
