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

PHONE_STYLE = """
<style>
/* page background */
body {
  background: linear-gradient(135deg, #2fe273 0%, #09742a 100%) !important;
  min-height: 100vh;
}
/* the “phone” wrapper */
.stApp {
  background: linear-gradient(335deg, #2fe273 0%, #09742a 100%) !important;
  border-radius: 32px;
  max-width: 400px;
  min-height: 100vh;
  height: 100vh;
  overflow-y: auto;
  margin: 32px auto;
  box-shadow: 0 8px 32px rgba(60,60,60,0.25),
              0 1.5px 8px rgba(30,90,40,0.06);
  border: 3px solid #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
}

/* two-column grid helper */
.dashboard {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  width: 100%;
  padding: 10px 0;
}

/* card base with centered contents */
.card {
  border-radius: 16px;
  padding: 10px;
  color: white;
  box-shadow: 0 4px 10px rgba(0,0,0,0.15);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
/* subtle bright palette */
.blue   { background-color: #64B5F6; }  /* sky blue */
.red    { background-color: #E57373; }  /* soft red */
.green  { background-color: #81C784; }  /* mint green */
.purple { background-color: #BA68C8; }  /* lavender */

.card h2 {
  margin: 0;
  font-size: 24px;
}
.card small {
  display: block;
  margin-bottom: 6px;
  font-size: 18px;
  opacity: 0.9;
}
.card a {
  display: inline-block;
  background-color: rgba(255,255,255,0.15);
  border-radius: 20px;
  padding: 8px;
  font-size: 16px;
  color: black;
  text-decoration: none;
  transition: background-color 0.2s ease;
  margin-top: 8px;
}
.card a:hover {
  background-color: rgba(255,255,255,0.25);
}
</style>
"""

def apply_mobile_style():
    st.markdown(STYLE, unsafe_allow_html=True)

def apply_phone_style():
    """Apply the full mobile phone layout and card styling."""
    st.markdown(PHONE_STYLE, unsafe_allow_html=True)
