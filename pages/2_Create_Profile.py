import streamlit as st
import openai
import json
import os
from typing import List
from app_utils import load_api_key, apply_mobile_style

# ---------- API Key Configuration ---------- #
apply_mobile_style()
api_key = load_api_key(use_sidebar=False)
if not api_key:
    st.error("OpenAI API key required.")
    st.stop()
openai.api_key = api_key

# Directories for profiles and memory
PROFILE_DIR = 'profiles'
MEMORY_DIR = 'memory_profiles'
os.makedirs(PROFILE_DIR, exist_ok=True)
os.makedirs(MEMORY_DIR, exist_ok=True)

# Generate agent response
def generate_agent_response(config: dict, history: List[dict], docs_content: List[str]) -> str:
    persona_desc = config.get('persona_descriptions', 'No persona notes')
    system_lines = [
        f"Agent Type: {config['agent_type']}",
        f"Agent Role: {config['agent_role']}",
        f"Persona: {persona_desc}",
        f"Tone: {config['tone']}",
        f"Tools: {', '.join(config['tools']) or 'None'}",
        f"Interactive Modes: {', '.join(config['interactive_modes']) or 'None'}",
        f"Intent Shortcuts: {', '.join(config['intent_shortcuts']) or 'None'}",
        f"Formatting Preference: {config['format_pref']}",
    ]
    if config.get('external_data'):
        system_lines.append("External Data Access: Enabled")
    if docs_content:
        system_lines.append(f"Reference Docs ({len(docs_content)}):\n" + "\n".join(docs_content))

    system_prompt = "\n".join(system_lines)
    messages = [{'role': 'system', 'content': system_prompt}] + history
    resp = openai.ChatCompletion.create(
        model='gpt-4',
        messages=messages,
        temperature=config['temperature'],
        max_tokens=config['verbosity'],
    )
    return resp.choices[0].message.content

# ---------- UI Setup ---------- #
st.set_page_config(page_title='Parenting Agent', layout='centered')
st.title('🤖 Parenting Agent')

# Sidebar configuration form
with st.sidebar.form('config_form'):
    st.header('Agent Configuration')
    agent_type = st.selectbox('Agent Type', ['Parenting Coach', 'Emotional Regulator', 'Communication Trainer', 'Cognitive Scaffold'])
    agent_role = st.text_input('Agent Role', 'e.g., De-escalate sibling rivalry')
    persona_styles = st.multiselect('Persona Styles', ['Montessori', 'Gentle Parenting', 'Authoritative'])
    custom_notes_file = st.file_uploader('Upload Persona Notes', type=['txt'])
    custom_notes_text = custom_notes_file.read().decode('utf-8', errors='ignore') if custom_notes_file else ''
    persona_descriptions = ', '.join(persona_styles) + (f"\nCustom Notes:\n{custom_notes_text}" if custom_notes_text else '')
    tools = st.multiselect('Tool Integrations', ['Emotion Tracker', 'Schedule Builder', 'Story Generator', 'Role-play Simulator'])
    memory_option = st.radio('Memory Option', ['Session-only', 'Persistent'], index=0)
    uploaded_docs = st.file_uploader('Upload Reference Documents', accept_multiple_files=True)
    docs_content = []
    for doc in uploaded_docs or []:
        try:
            text = doc.read().decode('utf-8', errors='ignore')[:200]
            docs_content.append(f"{doc.name}: {text}...")
        except:
            docs_content.append(f"{doc.name}: (binary)")
    external_data = st.checkbox('External Data Access')
    st.markdown('---')
    st.subheader('Prompt Controls')
    temperature = st.slider('Temperature', 0.0, 1.0, 0.7)
