import streamlit as st
import os
import json
from app_utils import apply_mobile_style

apply_mobile_style()

st.title("📁 Saved Items")

PROFILE_DIR = "profiles"
CHAT_HISTORY_PATH = "chat_history.json"

profiles = []
if os.path.isdir(PROFILE_DIR):
    for filename in os.listdir(PROFILE_DIR):
        if filename.endswith('.json'):
            path = os.path.join(PROFILE_DIR, filename)
            try:
                data = json.load(open(path))
                data['__file'] = path
                profiles.append(data)
            except Exception as e:
                st.warning(f"Could not read {filename}: {e}")

if not profiles:
    st.info("No saved profiles found.")
else:
    profile_options = [p.get('profile_name') or os.path.basename(p['__file']) for p in profiles]
    idx = st.selectbox("Select a profile", range(len(profile_options)), format_func=lambda i: profile_options[i])
    profile = profiles[idx]
    st.subheader("Profile Details")
    photo = profile.get('profile_photo')
    if photo and os.path.exists(photo):
        st.image(photo, width=150)
    pname = profile.get('parent_name')
    cname = profile.get('child_name')
    cage = profile.get('child_age')
    if pname or cname:
        st.write(f"**Parent:** {pname or 'N/A'}")
        st.write(f"**Child:** {cname or 'N/A'}" + (f" (age {cage})" if cage is not None else ''))
    st.json({k: v for k, v in profile.items() if not k.startswith('__') and k not in ['profile_photo','parent_name','child_name','child_age']})
   
    if st.button("Activate Profile"):
        st.session_state['active_profile'] = profile
        st.success("Profile loaded. Switch to 'Parent Chat' to begin chatting.")

    st.markdown('---')
    st.subheader('Recent Chats')
    if os.path.exists(CHAT_HISTORY_PATH):
        all_history = json.load(open(CHAT_HISTORY_PATH))
        pname = profile.get('profile_name') or os.path.basename(profile['__file'])
        chats = all_history.get(pname, [])
        if chats:
            for item in reversed(chats[-10:]):
                st.markdown(f"<p style='color:#fff;'><strong>You:</strong> {item['q']}</p>", unsafe_allow_html=True)
                st.markdown(f"<div class='answer-box'>{item['a']}</div>", unsafe_allow_html=True)
                st.markdown('<hr>', unsafe_allow_html=True)
            if st.button('Delete History'):
                all_history[pname] = []
                with open(CHAT_HISTORY_PATH, 'w') as f:
                    json.dump(all_history, f, indent=2)
                st.success('History cleared!')
                st.experimental_rerun()
        else:
            st.write('No chat history for this profile.')
    else:
        st.write('No chat history found.')
