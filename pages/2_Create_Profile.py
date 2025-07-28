import os
import json
from typing import List
import streamlit as st
import openai

# OpenAI key from Streamlit secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Directory for storing saved agent profiles
MEMORY_DIR = "memory_profiles"
os.makedirs(MEMORY_DIR, exist_ok=True)


def generate_agent_response(config: dict, history: List[dict]) -> str:
    """Generate a chat response from OpenAI using the given config and history."""
    system_prompt = (
        f"You are a {config['agent_type']} specializing in {config['agent_role']} "
        f"with persona {config['persona_descriptions']}."
    )
    messages = [{'role': 'system', 'content': system_prompt}] + history
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        temperature=config['temperature'],
        max_tokens=500,
    )
    return response.choices[0].message.content


st.title("🧬 Agent Builder")

# Sidebar configuration UI
with st.sidebar:
    st.header("Agent Configuration")
    agent_type = st.selectbox(
        "Agent Type",
        ["Parenting Coach", "Emotional Regulator", "Communication Trainer", "Cognitive Scaffold"],
    )
    agent_role = st.text_input("Agent Role (Task)", "e.g., De-escalate sibling rivalry")
    persona = st.multiselect(
        "Persona Styles",
        ["Montessori", "Gentle Parenting", "Authoritative"],
        help="Mix & match or upload custom notes below",
    )
    custom_notes = st.file_uploader("Upload Persona Notes (txt)", type=["txt"])
    tools = st.multiselect(
        "Tool Integrations",
        ["Emotion Tracker", "Schedule Builder", "Story Generator", "Role-play Simulator"],
    )
    memory_option = st.radio("Memory Option", ["Session-only", "Persistent per profile"], index=0)
    uploaded_docs = st.file_uploader("Upload Reference Documents", accept_multiple_files=True)
    external_data = st.checkbox("Enable External Data Access", value=False)
    st.markdown("---")
    st.subheader("Prompt Controls")
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    verbosity = st.slider("Verbosity (max tokens)", 100, 2000, 500)
    tone = st.selectbox("Tone", ["Nurturing", "Playful", "Firm"])
    st.markdown("---")
    st.subheader("Interaction Modes")
    interactive_modes = st.multiselect(
        "Modes",
        ["Co-Play Simulation", "Role Reversal", "Story Prompting", "Joint Reflections"],
    )
    intent_shortcuts = st.multiselect(
        "Intent Shortcuts",
        [
            "Connect",
            "Grow",
            "Explore",
            "Resolve",
            "Support + Ask",
            "Imagine",
            "Challenge",
            "Reflect",
            "Rehearse",
        ],
    )
    format_pref = st.selectbox(
        "Formatting",
        ["List", "Table", "Steps", "Dialogue Script", "Visual Summary"],
    )
    enable_feedback = st.checkbox("Enable Feedback Loop", value=True)
    audio_upload = st.file_uploader("Upload Audio for Voice Integration", type=["mp3", "wav"])
    st.markdown("---")
    save_profile = st.button("Save Profile")

# Save profile to disk when requested
if save_profile:
    profile = {
        "agent_type": agent_type,
        "agent_role": agent_role,
        "persona_descriptions": persona,
        "tools": tools,
        "memory_option": memory_option,
        "external_data": external_data,
        "temperature": temperature,
        "verbosity": verbosity,
        "tone": tone,
        "interactive_modes": interactive_modes,
        "intent_shortcuts": intent_shortcuts,
        "format_pref": format_pref,
    }
    fname = os.path.join(MEMORY_DIR, f"profile_{agent_type.replace(' ', '_')}.json")
    with open(fname, "w") as f:
        json.dump(profile, f)
    st.sidebar.success(f"Profile saved to {fname}")

# Conversation history stored in the session
if "history" not in st.session_state:
    st.session_state.history = []

st.header("Chat")
user_input = st.text_input("Your message:")
if st.button("Send") and user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    config = {
        "agent_type": agent_type,
        "agent_role": agent_role,
        "persona_descriptions": persona,
        "temperature": temperature,
    }
    with st.spinner("Generating response..."):
        reply = generate_agent_response(config, st.session_state.history)
    st.session_state.history.append({"role": "assistant", "content": reply})

for msg in st.session_state.history:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Agent:** {msg['content']}")

# Simple feedback loop
if enable_feedback and st.session_state.history:
    rating = st.slider("Rate the last response", 1, 5, key="feedback_slider")
    if st.button("Submit Feedback"):
        st.success(f"Thanks for your feedback: {rating}/5")
