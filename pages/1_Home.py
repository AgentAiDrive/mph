import streamlit as st
import os
import json

# --- Styles for “cards” ---
st.markdown("""
    <style>
      .card {
        background-color: #f0f4f8;
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        margin-bottom: 16px;
      }
      .card-blue { background-color: #e3f2fd; }
      .card-green { background-color: #e8f5e9; }
    </style>
""", unsafe_allow_html=True)


# --- Header with logo and title ---
col1, col2 = st.columns(2)
with col1:
    st.image("MYPARENTHELPERS_512x512.png", width=80)
with col2:
    st.header("pAIrents Agents")
st.markdown("---")


# --- Intro text ---
st.markdown(
    """
    Create personalized “pAIrents agents” personas based on books, 
    styles, or experts within a context-prompt generator.
    """
)
st.markdown("---")


# --- Navigation links (4 columns) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/2_Create_Profile.py", label="Create Profile", icon="🧬")
with col2:
    st.page_link("pages/3_Chat_Helper.py",   label="Parent Chat",    icon="💬")
with col3:
    st.page_link("pages/4_Saved_Items.py",   label="Saved Items",    icon="📁")
with col4:
    st.page_link("pages/5_Support.py",       label="Support",        icon="🆘")
st.markdown("---")


# --- Active profile display ---
active_profile = st.session_state.get("active_profile")
if active_profile:
    name = active_profile.get("profile_name") or active_profile.get("agent_role", "Profile")
    st.subheader(f"🟢 Active Profile: {name}")
else:
    st.subheader("No profile active.")
st.markdown("---")


# --- Paths for profiles and chat history ---
PROFILE_DIR        = "profiles"
CHAT_HISTORY_PATH  = "chat_history.json"

# --- Wrapped card container for both columns ---
st.markdown('<div class="card-container">', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Saved Profiles")
    profiles = []
    if os.path.isdir("profiles"):
        for fn in os.listdir("profiles"):
            if fn.endswith(".json"):
                profiles.append(fn[:-5])
    if profiles:
        for p in profiles:
            st.markdown(f"- {p}")
    else:
        st.write("None")

with col2:
    st.markdown("### Saved Chats")
    if os.path.exists("chat_history.json"):
        try:
            with open("chat_history.json") as f:
                history = json.load(f)
            for key, messages in history.items():
                st.markdown(f"- {key} ({len(messages)} messages)")
        except Exception as e:
            st.write(f"Error reading chat history: {e}")
    else:
        st.write("None")

st.markdown('</div>', unsafe_allow_html=True)
