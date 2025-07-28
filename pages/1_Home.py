import streamlit as st
from PIL import Image
import os
import json


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header ("Pairents Agents")
with col2:
    st.image("MYPARENTHELPERS_512x512.png", width=80)
with col3:
    st.page_link("pages/4_Saved_Items.py", label="Saved Items", icon="📁")
with col4:
    st.page_link("pages/5_Support.py", label="Support", icon="🆘")
st.markdown("---")


col1, col2, col3, col4 = st.columns(4)
with col1:
    st.page_link("pages/2_Create_Profile.py", label="Create Profile", icon="🧬")
with col2:
    st.page_link("pages/3_Chat_Helper.py", label="Parent Chat", icon="💬")
with col3:
    st.page_link("pages/4_Saved_Items.py", label="Saved Items", icon="📁")
with col4:
    st.page_link("pages/5_Support.py", label="Support", icon="🆘")
st.markdown("---")
st.image("MYPARENTHELPERS_512x512.png", width=80)
st.markdown("""
Create personalized AI parenting assistants based on books, styles, or experts.
Start by creating a profile with your parenting approach and your child’s details.
"""
)

active_profile = st.session_state.get("active_profile")
if active_profile:
    name = active_profile.get("profile_name") or active_profile.get(
        "agent_role", "Profile"
    )
    st.subheader(f"🟢 Active Profile: {name}")
else:
    st.subheader("No profile active.")

PROFILE_DIR = "profiles"
CHAT_HISTORY_PATH = "chat_history.json"

st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Saved Profiles")
    profiles = []
    if os.path.isdir(PROFILE_DIR):
        for fn in os.listdir(PROFILE_DIR):
            if fn.endswith(".json"):
                profiles.append(fn[:-5])
    if profiles:
        for p in profiles:
            st.markdown(f"- {p}")
    else:
        st.write("None")

with col2:
    st.markdown("### Saved Chats")
    if os.path.exists(CHAT_HISTORY_PATH):
        try:
            history = json.load(open(CHAT_HISTORY_PATH))
            for key in history.keys():
                st.markdown(f"- {key} ({len(history[key])} messages)")
        except Exception as e:
            st.write(f"Error reading chat history: {e}")
    else:
        st.write("None")
