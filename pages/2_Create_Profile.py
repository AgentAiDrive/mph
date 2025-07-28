import streamlit as st
import openai
import json
import os
from typing import List

# ---------- API Key Configuration ---------- #
# Attempt to load API key from Streamlit secrets
api_key = None
if "openai" in st.secrets and "api_key" in st.secrets["openai"]:
    api_key = st.secrets["openai"]["api_key"]
# Fallback to environment variable
if not api_key:
    api_key = os.getenv("OPENAI_API_KEY", "")
# In-app prompt as last resort
if not api_key:
    api_key = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
# Stop if no key provided
if not api_key:
    st.sidebar.error(
        "OpenAI API key not configured. Add to secrets.toml under [openai] api_key, set the OPENAI_API_KEY env var, or enter above."
    )
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
st.set_page_config(page_title='Parenting Agent', layout='wide')
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
    verbosity = st.slider('Max Tokens', 100, 2000, 500)
    tone = st.selectbox('Tone', ['Nurturing', 'Playful', 'Firm'])
    st.markdown('---')
    st.subheader('Interactions')
    interactive_modes = st.multiselect('Modes', ['Co-Play Simulation', 'Role Reversal', 'Story Prompting', 'Joint Reflections'])
    intent_shortcuts = st.multiselect('Shortcuts', ['Connect', 'Grow', 'Explore', 'Resolve', 'Support + Ask', 'Imagine', 'Challenge', 'Reflect', 'Rehearse'])
    format_pref = st.selectbox('Format', ['List', 'Table', 'Steps', 'Dialogue', 'Visual Summary'])
    st.markdown('---')
    enable_feedback = st.checkbox('Enable Feedback Loop', value=True)
    audio_file = st.file_uploader('Upload Audio', type=['mp3','wav'])
    save_profile = st.form_submit_button('Save Profile')

# Save profile
if save_profile:
    profile = {k: v for k, v in locals().items() if k in ['agent_type','agent_role','persona_styles','custom_notes_text','tools','memory_option','external_data','temperature','verbosity','tone','interactive_modes','intent_shortcuts','format_pref']}
    fname = os.path.join(PROFILE_DIR, f"profile_{agent_type}_{agent_role}.json")
    with open(fname, 'w') as f:
        json.dump(profile, f)
    st.sidebar.success(f'Saved: {fname}')

# Load session history or persistent memory
profile_key = f"{agent_type}_{agent_role}"
mem_file = os.path.join(MEMORY_DIR, f"{profile_key}.json")
if 'history' not in st.session_state:
    if memory_option=='Persistent' and os.path.exists(mem_file):
        st.session_state.history = json.load(open(mem_file))
    else:
        st.session_state.history = []

# Chat interface
st.header('Chat')
user_input = st.text_input('Your message')
if st.button('Send') and user_input:
    st.session_state.history.append({'role':'user','content':user_input})
    config = dict(agent_type=agent_type,agent_role=agent_role,persona_descriptions=persona_descriptions,tools=tools,external_data=external_data,temperature=temperature,verbosity=verbosity,tone=tone,interactive_modes=interactive_modes,intent_shortcuts=intent_shortcuts,format_pref=format_pref)
    reply = generate_agent_response(config, st.session_state.history, docs_content)
    st.session_state.history.append({'role':'assistant','content':reply})
    if memory_option=='Persistent':
        json.dump(st.session_state.history, open(mem_file,'w'))

# Display convo
for msg in st.session_state.history:
    speaker = 'You' if msg['role']=='user' else 'Agent'
    st.markdown(f"**{speaker}:** {msg['content']}")

# Feedback
if enable_feedback and st.session_state.history:
    st.markdown('---')
    rating = st.slider('Rate response',1,5)
    if st.button('Submit Feedback'):
        st.success(f'Thanks: {rating}/5')
