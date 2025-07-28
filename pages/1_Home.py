import streamlit as st
import os
import json

# --- Styles for “card container” ---
st.markdown("""
    <style>
      .card-container {
        background-color: #e8f5e9;     /* light green */
        padding: 16px;
        border-radius: 12px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        margin-bottom: 16px;
      }
    </style>
""", unsafe_allow_html=True)


# ... your header / nav / active profile code here ...


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
