import streamlit as st
import os
import json

# --- Custom CSS ---
st.markdown("""
    <style>
    .dashboard {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        padding: 10px;
        margin-top: 60px;          /* leave room for top nav */
    }
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

    /* Top nav (re-used bottom-nav styles but pinned to top) */
    .bottom-nav {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: space-around;
        background: #ffffff;
        padding: 12px 0;
        border-bottom: 1px solid #eee;
        z-index: 100;
    }
    .nav-icon {
        font-size: 24px;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# --- Top Navigation ---
st.markdown("""
    <div class="bottom-nav">
      <a href="?page=2_Create_Profile" class="nav-icon">🧬</a>
      <a href="?page=3_Chat_Helper"   class="nav-icon">💬</a>
      <a href="?page=4_Saved_Items"   class="nav-icon">📁</a>
      <a href="?page=5_Support"       class="nav-icon">🆘</a>
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
            <a href="{link}">{btn}</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
