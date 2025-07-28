import streamlit as st
import openai
import os, json
from app_utils import load_api_key, apply_mobile_style

st.set_page_config(page_title="Parent Chat", layout="centered")
apply_mobile_style()
openai.api_key = load_api_key()
if not openai.api_key:
    st.sidebar.error("OpenAI API key required.")
    st.stop()

PROFILE_PATH = "profiles.json"
CHAT_HISTORY_PATH = "chat_history.json"

# Response shortcut configuration
SHORTCUTS = [
    "💬 DEFAULT",
    "🤝 CONNECT",
    "🌱 GROW",
    "🔍 EXPLORE",
    "🛠 RESOLVE",
    "❤ SUPPORT",
]
EMOJIS = {
    "💬 DEFAULT": "💬",
    "🤝 CONNECT": "🤝",
    "🌱 GROW": "🌱",
    "🔍 EXPLORE": "🔍",
    "🛠 RESOLVE": "🛠",
    "❤ SUPPORT": "❤",
}
EXTRA_MAP = {
    "🤝 CONNECT": " Help explain with examples.",
    "🌱 GROW": " Offer advanced strategies.",
    "🔍 EXPLORE": " Facilitate age-appropriate Q&A.",
    "🛠 RESOLVE": " Provide step-by-step resolution.",
    "❤ SUPPORT": " Offer empathetic support.",
}


def build_system_message(profile: dict, response_type: str) -> str:
    """Construct a system prompt based on old or new profile formats."""
    # New advanced profile format
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
def get_active_profile():

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
st.markdown(f"**Talking as:** {display_name}")

st.session_state.setdefault("shortcut", "💬 DEFAULT")
st.session_state.setdefault("last_answer", "")

query = st.text_area("What's your parenting challenge?")

if st.session_state.last_answer:
    st.markdown(f"<div class='answer-box'>{st.session_state.last_answer}</div>", unsafe_allow_html=True)

cols = st.columns(len(SHORTCUTS))
for i, sc in enumerate(SHORTCUTS):
    with cols[i]:
        if st.button(EMOJIS[sc], key=f"sc_{i}"):
            st.session_state.shortcut = sc

if st.button("Send") and query:
    rtype_map = {
        "💬 DEFAULT": "Default",
        "🤝 CONNECT": "Connect",
        "🌱 GROW": "Grow",
        "🔍 EXPLORE": "Explore",
        "🛠 RESOLVE": "Resolve",
        "❤ SUPPORT": "Support",
    }
    rtype = rtype_map.get(st.session_state.shortcut, "Default")
    system_message = build_system_message(profile, rtype)
    prompt = query + EXTRA_MAP.get(st.session_state.shortcut, "")
    with st.spinner("Thinking..."):
        completion = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
        )
        reply = completion.choices[0].message.content
    st.session_state.last_answer = reply
    st.markdown(f"<div class='answer-box'>{reply}</div>", unsafe_allow_html=True)
    profile_key = profile.get('profile_name') or f"{profile.get('agent_type','')}_{profile.get('agent_role','default')}"
    save_chat(profile_key, query, reply)

with st.expander("🕓 View Chat History"):
    profile_key = profile.get('profile_name') or f"{profile.get('agent_type','')}_{profile.get('agent_role','default')}"
    history = load_chat_history(profile_key)
    for item in reversed(history[-10:]):
        st.markdown(f"**You:** {item['q']}")
        st.markdown(f"**Helper:** {item['a']}")
        st.markdown("---")
