import streamlit as st
import openai
import os
import json
from app_utils import load_api_key, apply_mobile_style

st.set_page_config(page_title="Parent Chat", layout="centered")
apply_mobile_style()
openai.api_key = load_api_key(use_sidebar=False)
if not openai.api_key:
    st.error("OpenAI API key required.")
    st.stop()

PROFILE_PATH = "profiles.json"
CHAT_HISTORY_PATH = "chat_history.json"


def build_system_message(profile: dict, response_type: str) -> str:
    """Construct a system prompt based on old or new profile formats."""
    if "agent_type" in profile:
        lines = [
            f"Agent Type: {profile.get('agent_type')}",
            f"Agent Role: {profile.get('agent_role')}",
            f"Tone: {profile.get('tone')}",
        ]
        persona = profile.get("persona_descriptions")
        if persona:
            lines.append(f"Persona: {persona}")
        tools = ", ".join(profile.get("tools", []))
        if tools:
            lines.append(f"Tools: {tools}")
        modes = ", ".join(profile.get("interactive_modes", []))
        if modes:
            lines.append(f"Interactive Modes: {modes}")
        intents = ", ".join(profile.get("intent_shortcuts", []))
        if intents:
            lines.append(f"Intent Shortcuts: {intents}")
        fmt = profile.get("format_pref")
        if fmt:
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

if response_type and query:
    system_message = build_system_message(profile, response_type)

    with st.spinner("Thinking..."):
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": query},
            ],
        )
        reply = completion.choices[0].message.content
        st.markdown("#### 📥 Response")
        st.write(reply)
        profile_key = profile.get('profile_name') or f"{profile.get('agent_type','')}_{profile.get('agent_role','default')}"
        save_chat(profile_key, query, reply)

with st.expander("🕓 View Chat History"):
    profile_key = profile.get('profile_name') or f"{profile.get('agent_type','')}_{profile.get('agent_role','default')}"
    history = load_chat_history(profile_key)
    for item in reversed(history[-10:]):
        st.markdown(f"**You:** {item['q']}")
        st.markdown(f"**Helper:** {item['a']}")
        st.markdown("---")

