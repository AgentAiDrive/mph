import streamlit as st
import os

KEY_FILE = "openai_key.txt"

def load_api_key():
    """Retrieve OpenAI API key from secrets, file, or sidebar input."""
    if "openai_api_key" in st.session_state:
        return st.session_state.openai_api_key

    key = None
    if "openai" in st.secrets and "api_key" in st.secrets["openai"]:
        key = st.secrets["openai"]["api_key"]
    if not key and os.getenv("OPENAI_API_KEY"):
        key = os.getenv("OPENAI_API_KEY")
    if not key and os.path.exists(KEY_FILE):
        try:
            key = open(KEY_FILE).read().strip()
        except Exception:
            key = None
    if not key:
        key = st.sidebar.text_input("Enter OpenAI API Key", type="password")
        remember = st.sidebar.checkbox("Remember key", key="remember_key")
        if key and remember:
            with open(KEY_FILE, "w") as f:
                f.write(key.strip())
    st.session_state.openai_api_key = key
    return key

STYLE = """
<style>
body {background: linear-gradient(135deg,#2fe273 0%,#09742a 100%) !important; min-height:100vh;}
.stApp {
  background: linear-gradient(335deg,#2fe273 0%,#09742a 100%) !important;
  border-radius: 32px; max-width: 400px; min-height: 100vh; height: 100vh;
  overflow-y: auto; margin: 32px auto; box-shadow: 0 8px 32px rgba(60,60,60,.25), 0 1.5px 8px rgba(30,90,40,.06);
  border: 3px solid #ffffff; display: flex; flex-direction: column; align-items: center; padding: 10px;
}
</style>
"""

def apply_mobile_style():
    st.markdown(STYLE, unsafe_allow_html=True)
