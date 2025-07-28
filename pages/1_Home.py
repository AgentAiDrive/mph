import streamlit as st

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    .dashboard {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        padding: 10px;
    }
    .card {
        background-color: #f0f4f8;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        color: white;
        text-align: center;
        font-weight: 600;
        font-size: 18px;
    }
    .red { background-color: #f94144; }
    .blue { background-color: #577590; }
    .orange { background-color: #f3722c; }
    .purple { background-color: #6a4c93; }
    .teal { background-color: #43aa8b; }
    .green { background-color: #90be6d; }
    </style>
""", unsafe_allow_html=True)

# --- Dashboard Cards ---
st.markdown('<div class="dashboard">', unsafe_allow_html=True)

st.markdown('<div class="card red">❤️ 124 bpm<br><small>Heart Rate</small></div>', unsafe_allow_html=True)
st.markdown('<div class="card blue">😴 8 hrs<br><small>Sleep</small></div>', unsafe_allow_html=True)
st.markdown('<div class="card orange">🔥 382 kcal<br><small>Calories</small></div>', unsafe_allow_html=True)
st.markdown('<div class="card purple">🚶‍♂️ 10,701<br><small>Steps</small></div>', unsafe_allow_html=True)
st.markdown('<div class="card teal">🏃‍♀️ 6.3 km<br><small>Activity</small></div>', unsafe_allow_html=True)
st.markdown('<div class="card green">🧘 12.5 hrs<br><small>Mindfulness</small></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Bottom Navigation ---
st.markdown("""
    <style>
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

    <div class="bottom-nav">
        <div class="nav-icon">🏠</div>
        <div class="nav-icon">📊</div>
        <div class="nav-icon">👤</div>
    </div>
""", unsafe_allow_html=True)
