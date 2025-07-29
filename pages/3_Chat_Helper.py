import streamlit as st
import os
import json
from openai import OpenAI
from app_utils import apply_mobile_style, get_openai_key

# --- Streamlit setup ---
st.set_page_config(page_title="Parent Chat", layout="centered")
apply_mobile_style()

# --- OpenAI API Setup ---
api_key = get_openai_key()
if not api_key:
    st.error("OpenAI API key required.")
    st.stop()

client = OpenAI(api_key=api_key)

# --- File paths ---
PROFILE_PATH = "profiles.json"
CHAT_HISTORY_PATH = "chat_history.json"

# --- Utility Functions ---
def build_system_message(profile: dict, response_type: str) -> str:
    if "agent_type" in profile:
        lines = [
            f"Agent Type: {profile.get('agent_type')}",
            f"Agent Role: {profile.get('agent_role')}",
            f"Tone: {profile.get('tone')}",
        ]
        if persona := profile.get("persona_descriptions"):
            lines.append(f"Persona: {persona}")
        if tools := ", ".join(profile.get("tools", [])):
            lines.append(f"Tools: {tools}")
        if modes := ", ".join(profile.get("interactive_modes", [])):
            lines.append(f"Interactive Modes: {modes}")
        if intents := ", ".join(profile.get("intent_shortcuts", [])):
            lines.append(f"Intent Shortcuts: {intents}")
        if fmt := profile.get("format_pref"):
            lines.append(f"Formatting Preference: {fmt}")
        if profile.get('parent_name'):
            lines.append(f"Parent Name: {profile['parent_name']}")
        if profile.get('child_name'):
            lines.append(f"Child Name: {profile['child_name']}")
        if profile.get('child_age'):
            lines.append(f"Child Age: {profile['child_age']}")
        if profile.get("external_data"):
            lines.append("External Data Access: Enabled")
        lines.append(f"Respond with a {response_type}-type answer.")
        return "\n".join(lines)

    return (
        f"You are a parenting assistant using the \"{profile['source_name']}\" "
        f"({profile['source_type']}) style.\n"
        f"Respond with a {response_type}-type answer suitable for a child age "
        f"{profile['child_age']}.\n"
        f"Use parent name: {profile['parent_name']}, and child name: {profile['child_name']}"
    )

def get_active_profile():
    return st.session_state.get("active_profile")

def load_chat_history(profile_name):
    if os.path.exists(CHAT_HISTORY_PATH):
        with open(CHAT_HISTORY_PATH, "r") as f:
            all_history = json.load(f)
        return all_history.get(profile_name, [])
    return []

def save_chat(profile_name, question, answer):
    all_history = {}
    if os.path.exists(CHAT_HISTORY_PATH):
        with open(CHAT_HISTORY_PATH, "r") as f:
            all_history = json.load(f)
    all_history.setdefault(profile_name, []).append({"q": question, "a": answer})
    with open(CHAT_HISTORY_PATH, "w") as f:
        json.dump(all_history, f, indent=2)

# --- App UI ---
st.title("💬 Parent Chat")
profile = get_active_profile()

if not profile:
    st.warning("Please load a profile first.")
    st.stop()

display_name = profile.get('profile_name') or profile.get('agent_role', 'Profile')
st.subheader(f"👨‍👩‍👧 Talking as: {display_name}")
query = st.text_area("What's your parenting challenge?")
col1, col2, col3, col4, col5 = st.columns(5)
response_type = None
if col1.button("Explore"):
    response_type = "Explore"
if col2.button("Connect"):
    response_type = "Connect"
if col3.button("Grow"):
    response_type = "Grow"
if col4.button("Support"):
    response_type = "Support"
if col5.button("Resolve"):
    response_type = "Resolve"

profile_key = profile.get('profile_name') or f"{profile.get('agent_type','')}_{profile.get('agent_role','default')}"

if response_type and query:
    system_message = build_system_message(profile, response_type)
    try:
        with st.spinner("Thinking..."):
            completion = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": query},
                ],
            )
            reply = completion.choices[0].message.content
            st.markdown("#### 📥 Response")
            st.write(reply)
            save_chat(profile_key, query, reply)
    except Exception as e:
        st.error(f"Something went wrong: {e}")
        if st.button("🔁 Retry"):
            st.rerun()

# --- History Viewer ---
with st.expander("🕓 View Chat History"):
    history = load_chat_history(profile_key)
    for item in reversed(history[-10:]):
        st.markdown(f"**You:** {item['q']}")
        st.markdown(f"**Helper:** {item['a']}")
        st.markdown("---")
