import streamlit as st
import openai
import os, json

openai.api_key = st.secrets["openai"]["api_key"]

PROFILE_PATH = "profiles.json"
CHAT_HISTORY_PATH = "chat_history.json"

def get_active_profile():
    return st.session_state.get("active_profile", None)

def load_chat_history(profile_name):
    if os.path.exists(CHAT_HISTORY_PATH):
        all_history = json.load(open(CHAT_HISTORY_PATH))
        return all_history.get(profile_name, [])
    return []

def save_chat(profile_name, question, answer):
    all_history = {}
    if os.path.exists(CHAT_HISTORY_PATH):
        all_history = json.load(open(CHAT_HISTORY_PATH))
    if profile_name not in all_history:
        all_history[profile_name] = []
    all_history[profile_name].append({"q": question, "a": answer})
    with open(CHAT_HISTORY_PATH, "w") as f:
        json.dump(all_history, f, indent=2)

st.title("💬 Parent Chat")
profile = get_active_profile()

if not profile:
    st.warning("Please load a profile first.")
    st.stop()

st.subheader(f"👨‍👩‍👧 Talking as: {profile['profile_name']}")
query = st.text_area("What's your parenting challenge?")
col1, col2, col3, col4, col5 = st.columns(5)
response_type = None
if col1.button("Explore"): response_type = "Explore"
if col2.button("Connect"): response_type = "Connect"
if col3.button("Grow"):    response_type = "Grow"
if col4.button("Support"): response_type = "Support"
if col5.button("Resolve"): response_type = "Resolve"

if response_type and query:
    system_message = f"""You are a parenting assistant using the "{profile['source_name']}" ({profile['source_type']}) style.
Respond with a {response_type}-type answer suitable for a child age {profile['child_age']}.
Use parent name: {profile['parent_name']}, and child name: {profile['child_name']}."""

    with st.spinner("Thinking..."):
        completion = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": query}
            ]
        )
        reply = completion.choices[0].message.content
        st.markdown("#### 📥 Response")
        st.write(reply)
        save_chat(profile['profile_name'], query, reply)

with st.expander("🕓 View Chat History"):
    history = load_chat_history(profile['profile_name'])
    for item in reversed(history[-10:]):
        st.markdown(f"**You:** {item['q']}")
        st.markdown(f"**Helper:** {item['a']}")
        st.markdown("---")
