import streamlit as st
import json, os, uuid
from PIL import Image

PROFILE_PATH = "profiles.json"
IMAGE_DIR = "images"
os.makedirs(IMAGE_DIR, exist_ok=True)

def load_profiles():
    if os.path.exists(PROFILE_PATH):
        with open(PROFILE_PATH) as f:
            return json.load(f)
    return []

def save_profiles(profiles):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profiles, f, indent=2)

def save_new_profile(profile):
    profiles = load_profiles()
    profiles.append(profile)
    save_profiles(profiles)

st.title("🧬 Manage Parenting Profiles")

with st.expander("➕ Create New Profile"):
    with st.form("create_profile"):
        profile = {
            "source_type": st.selectbox("Parenting Source Type", ["Book", "Expert", "Style"]),
            "source_name": st.text_input("Source Name"),
            "child_age": st.number_input("Child’s Age", 0, 18),
            "parent_name": st.text_input("Parent’s Name"),
            "child_name": st.text_input("Child’s Name"),
            "profile_name": st.text_input("Profile Name")
        }

        uploaded_file = st.file_uploader("Upload Profile Picture", type=["png", "jpg", "jpeg"])
        if uploaded_file:
            file_ext = uploaded_file.name.split(".")[-1]
            image_filename = f"{uuid.uuid4()}.{file_ext}"
            image_path = os.path.join(IMAGE_DIR, image_filename)
            with open(image_path, "wb") as f:
                f.write(uploaded_file.read())
            profile["image_path"] = image_path
        else:
            profile["image_path"] = None

        if st.form_submit_button("💾 Save Profile"):
            save_new_profile(profile)
            st.success("✅ Profile saved.")
            st.session_state.active_profile = profile

st.subheader("📂 Your Saved Profiles")
profiles = load_profiles()
if "edit_index" not in st.session_state:
    st.session_state.edit_index = None

if profiles:
    for idx, p in enumerate(profiles):
        col1, col2 = st.columns([7, 3])
        with col1:
            st.markdown(f"**{p['profile_name']}** — {p['source_type']}: _{p['source_name']}_ | Age: {p['child_age']}")
            if p.get("image_path") and os.path.exists(p["image_path"]):
                st.image(p["image_path"], width=80)
        with col2:
            if st.button("✏️ Edit", key=f"edit_{idx}"):
                st.session_state.edit_index = idx
            if st.button("🗑️ Delete", key=f"delete_{idx}"):
                confirm = st.radio(f"Delete {p['profile_name']}?", ["No", "Yes"], index=0, key=f"confirm_{idx}")
                if confirm == "Yes":
                    if p.get("image_path") and os.path.exists(p["image_path"]):
                        os.remove(p["image_path"])
                    profiles.pop(idx)
                    save_profiles(profiles)
                    st.success("🗑️ Profile deleted.")
                    st.session_state.edit_index = None
                    st.experimental_rerun()
            if st.button("📤 Load", key=f"load_{idx}"):
                st.session_state.active_profile = p
                st.success(f"✅ Loaded profile: {p['profile_name']}")
else:
    st.info("No saved profiles found.")
