import streamlit as st
import json
import os
from app_utils import load_api_key, apply_mobile_style

# Apply mobile style and check API key
apply_mobile_style()
api_key = load_api_key()
if not api_key:
    st.sidebar.error("OpenAI API key required.")
    st.stop()

PROFILE_DIR = "profiles"
os.makedirs(PROFILE_DIR, exist_ok=True)

st.set_page_config(page_title="Create Profile", layout="centered")
st.title("👤 Create Profile")

with st.form("profile_form"):
    profile_name = st.text_input("Profile Name")
    agent_type = st.selectbox(
        "Agent Type",
        ["Parenting Coach", "Emotional Regulator", "Communication Trainer", "Cognitive Scaffold"],
    )
    agent_role = st.text_input("Agent Role", "e.g., De-escalate sibling rivalry")
    persona_styles = st.multiselect(
        "Persona Styles", ["Montessori", "Gentle Parenting", "Authoritative"]
    )
    persona_notes = st.text_area("Additional Persona Notes")
    tools = st.multiselect(
        "Tool Integrations",
        ["Emotion Tracker", "Schedule Builder", "Story Generator", "Role-play Simulator"],
    )
    memory_option = st.radio("Memory Option", ["Session-only", "Persistent"], index=0)
    tone = st.selectbox("Tone", ["Nurturing", "Playful", "Firm"])
    interactive_modes = st.multiselect(
        "Modes",
        ["Co-Play Simulation", "Role Reversal", "Story Prompting", "Joint Reflections"],
    )
    intent_shortcuts = st.multiselect(
        "Shortcuts",
        ["Connect", "Grow", "Explore", "Resolve", "Support + Ask", "Imagine", "Challenge", "Reflect", "Rehearse"],
    )
    format_pref = st.selectbox(
        "Format", ["List", "Table", "Steps", "Dialogue", "Visual Summary"]
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    verbosity = st.slider("Max Tokens", 100, 2000, 500)
    external_data = st.checkbox("External Data Access")
    submitted = st.form_submit_button("Save Profile")

if submitted:
    profile = {
        "profile_name": profile_name.strip() or None,
        "agent_type": agent_type,
        "agent_role": agent_role,
        "persona_descriptions": ", ".join(persona_styles) + ("\n" + persona_notes if persona_notes else ""),
        "tools": tools,
        "memory_option": memory_option,
        "tone": tone,
        "interactive_modes": interactive_modes,
        "intent_shortcuts": intent_shortcuts,
        "format_pref": format_pref,
        "temperature": temperature,
        "verbosity": verbosity,
        "external_data": external_data,
    }

    fname = profile_name.strip() or f"{agent_type}_{agent_role}".replace(" ", "_")
    path = os.path.join(PROFILE_DIR, f"{fname}.json")
    with open(path, "w") as f:
        json.dump(profile, f, indent=2)
    st.session_state["active_profile"] = profile
    st.success(f"Profile saved to {path}")
