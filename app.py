import streamlit as st
import time
from datetime import datetime
from PIL import Image
import os

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="HBD AFFU 🌙", page_icon="🐼", layout="wide")

# --- 2. THE GRAND DESIGN (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), 
                    url('https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-attachment: fixed;
    }
    .nickname {
        font-family: 'serif';
        background: -webkit-linear-gradient(#fff, #ff9a9e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 80px;
        text-align: center;
        font-weight: bold;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 20px;
        padding: 20px;
        text-align: center;
        color: white;
        margin-bottom: 20px;
    }
    .grand-letter {
        background: #fffdf5;
        padding: 40px;
        border-radius: 10px;
        border: 2px solid #d4af37;
        color: #1a1a1a;
        font-family: 'Georgia', serif;
        max-width: 700px;
        margin: auto;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("🌙 Affu's 19th")
    page = st.radio("Go to:", ["The Grand Opening", "Memory Lane", "The Luxury Boutique", "A Royal Letter"])

# --- 4. NAVIGATION LOGIC ---
if page == "The Grand Opening":
    st.markdown('<p class="nickname">AFFU</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center; color:white; font-size:20px; letter-spacing:3px;">HAPPY 19TH BIRTHDAY</p>', unsafe_allow_html=True)
    
    target = datetime(2026, 3, 22, 0, 0, 0)
    now = datetime.now()
    diff = target - now

    if diff.total_seconds() > 0:
        cols = st.columns(4)
        days, hours, rem = diff.days, diff.seconds // 3600, diff.seconds % 3600
        mins, secs = rem // 60, rem % 60
        for col, val, lab in zip(cols, [days, hours, mins, secs], ["DAYS", "HOURS", "MINS", "SECS"]):
            col.markdown(f"<div class='glass-card'><h1>{val}</h1><p>{lab}</p></div>", unsafe_allow_html=True)
        time.sleep(1)
        st.rerun()
    else:
        st.balloons()
        st.snow()
        st.markdown("<h1 style='text-align:center; color: gold;'>👑 THE QUEEN HAS TURNED 19 👑</h1>", unsafe_allow_html=True)

elif page == "Memory Lane":
    st.markdown("<h1 style='text-align:center; color:white;'>📸 Memories</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i in range(1, 7):
        with cols[(i-1)%3]:
            # Check for various extensions
            found = False
            for ext in [".jpeg", ".jpg", ".png"]:
                if os.path.exists(f"photo{i}{ext}"):
                    st.image(f"photo{i}{ext}", use_container_width=True)
                    found = True
                    break
            if not found:
                st.markdown(f"<div class='glass-card'>Memory {i}<br>(Add photo)</div>", unsafe_allow_html=True)

elif page == "The Luxury Boutique":
    st.markdown("<h1 style='text-align:center; color:white;'>🛍️ Boutique</h1>", unsafe_allow_html=True)
    items = [
        ("Samba Burgundy", "👟"), ("Lip Gloss", "💄"), ("Panda Plush", "🐼"),
        ("Bouquet", "💐"), ("Designer Outfit", "👗"), ("Mystery Box", "🎁")
    ]
    cols = st.columns(3)
    for idx, (item, icon) in enumerate(items):
        with cols[idx % 3]:
            st.markdown(f"<div class='glass-card'><h2>{icon}</h2><h3>{item}</h3><p style='color:gold;'>FREE</p></div>", unsafe_allow_html=True)
            if st.button(f"Claim {item}", key=idx):
                st.toast(f"{item} reserved for Affu! ✨")

elif page == "A Royal Letter":
    pw = st.text_input("Enter Secret Word:", type="password")
    if pw.lower() == "panda":
        st.markdown("""
            <div class="grand-letter">
                <h2 style="color:#d81b60; text-align:center;">To My Best Human</h2>
                <p>Many more happy returns to the prettiest and loveliest <b>PANDA</b>.</p>
                <p>You're 19 now. Be brave, stay smiling like the moon (🌙), and know that Ashu is always here for you.</p>
                <p style="text-align:right;">— Ashu ❤️</p>
            </div>
        """, unsafe_allow_html=True)
