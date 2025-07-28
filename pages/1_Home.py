import streamlit as st

# --- Custom CSS ---
st.markdown("""
    <style>
    .dashboard {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        padding: 10px;
    }
    .card {
        border-radius: 16px;
        padding: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        position: relative;
    }
    .red { background-color: #f94144; }
    .blue { background-color: #577590; }
    .orange { background-color: #f3722c; }
    .purple { background-color: #6a4c93; }
    .teal { background-color: #43aa8b; }
    .green { background-color: #90be6d; }

    .card h2 {
        margin: 0;
        font-size: 24px;
    }

    .card small {
        display: block;
        margin-bottom: 12px;
        font-size: 14px;
    }

    .card button, .card a {
        background-color: rgba(255,255,255,0.15);
        border: none;
        padding: 8px 14px;
        border-radius: 8px;
        font-size: 14px;
        color: white;
        cursor: pointer;
        text-decoration: none;
        transition: background-color 0.2s ease;
    }

    .card button:hover, .card a:hover {
        background-color: rgba(255,255,255,0.25);
    }

    /* Bottom nav */
    .bottom-nav {
        position: fixed;
        bottom: 10px;
        left: 0;
        width: 100%;
        display: flex;
        justify-content: space-around;
        background: #ffffff;
        padding: 12px 0;
        border-top: 1px solid #eee;
    }
    .nav-icon {
        font-size: 24px;
    }
    </style>
""", unsafe_allow_html=True)

# --- Grid Layout with Buttons ---
st.markdown('<div class="dashboard">', unsafe_allow_html=True)

cards = [
    ("red", "❤️ 124 bpm", "Heart Rate", "#", "Details"),
    ("blue", "😴 8 hrs", "Sleep", "#", "Track Sleep"),
    ("orange", "🔥 382 kcal", "Calories", "#", "Burn History"),
    ("purple", "🚶‍♂️ 10,701", "Steps", "#", "Step Log"),
    ("teal", "🏃‍♀️ 6.3 km", "Activity", "#", "Workout Stats"),
    ("green", "🧘 12.5 hrs", "Mindfulness", "#", "Sessions"),
]

for color, title, subtitle, link, button_text in cards:
    st.markdown(f"""
        <div class="card {color}">
            <h2>{title}</h2>
            <small>{subtitle}</small>
            <a href="{link}" target="_blank">{button_text}</a>
        </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Bottom Navigation ---
st.markdown("""
    <div class="bottom-nav">
        <div class="nav-icon">🏠</div>
        <div class="nav-icon">📊</div>
        <div class="nav-icon">👤</div>
    </div>
""", unsafe_allow_html=True)
