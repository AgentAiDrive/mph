import streamlit as st
def get_openai_key():
    """Return the OpenAI API key from Streamlit secrets."""
    return st.secrets.get("openai_key", "YOUR_OPENAI_API_KEY")

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
