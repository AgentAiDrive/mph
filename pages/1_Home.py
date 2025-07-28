import streamlit as st
from PIL import Image
import os
import json

st.title("🏠 Welcome to My Parent Helpers")
st.image("MYPARENTHELPERS_512x512.png", width=160)
st.markdown(
    """
Create personalized AI parenting assistants based on books, styles, or experts.
Start by creating a profile with your parenting approach and your child’s details.
"""
)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("⚡ Quick Modes")
    modes = ["Explore", "Connect", "Grow", "Support", "Resolve"]
    for m in modes:
        if st.button(m):
            st.session_state["selected_mode"] = m
            st.switch_page("pages/3_Chat_Helper.py")

with col2:
    st.subheader("👤 Active Profile")
    profile = st.session_state.get("active_profile")
    if profile:
        name = profile.get("profile_name") or profile.get("agent_role", "Profile")
        st.write(name)
        if st.button("Open Chat"):
            st.switch_page("pages/3_Chat_Helper.py")
    else:
        st.write("No profile loaded.")

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.subheader("📁 Saved Profiles")
    profile_dir = "profiles"
    if os.path.isdir(profile_dir):
        files = [f for f in os.listdir(profile_dir) if f.endswith(".json")]
        if files:
            for f in files:
                display = os.path.splitext(f)[0]
                if st.button(display, key=f"prof_{f}"):
                    try:
                        data = json.load(open(os.path.join(profile_dir, f)))
                        st.session_state["active_profile"] = data
                        st.success(f"Loaded {display}")
                    except Exception as e:
                        st.error(f"Could not load {f}: {e}")
        else:
            st.write("No saved profiles.")
    else:
        st.write("No saved profiles.")

with col4:
    st.subheader("🗂️ Saved Chats")
    hist_path = "chat_history.json"
    if os.path.exists(hist_path):
        try:
            history = json.load(open(hist_path))
            if history:
                for pname in history.keys():
                    st.write(pname)
            else:
                st.write("No chats saved.")
        except Exception as e:
            st.error(f"Could not read chat history: {e}")
    else:
        st.write("No chats found.")

st.markdown("---")
if st.button("🚀 Create Profile"):
    st.switch_page("pages/2_Create_Profile.py")
