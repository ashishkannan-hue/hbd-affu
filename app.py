import streamlit as st
import time
from datetime import datetime
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
    /* Animation for flying elements */
    @keyframes fly-up {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
    }
    .floating-emoji {
        position: fixed;
        bottom: -100px;
        font-size: 28px;
        animation: fly-up 7s linear infinite;
        z-index: 999;
        pointer-events: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Fixed: Creating the 'page' variable first) ---
with st.sidebar:
    st.title("🌙 Affu's 19th")
    page = st.radio("Go to:", ["The Grand Opening", "Memory Lane", "The Luxury Boutique", "A Royal Letter"])

# --- 4. NAVIGATION LOGIC ---

if page == "The Grand Opening":
    st.markdown('<p class="nickname">AFFU</p>', unsafe_allow_html=True)
    
    # Target Date: March 22, 2026
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
        # --- THE REVEAL: GLOWING CAKE ---
        st.markdown("""
            <div style="text-align: center; padding: 40px;">
                <h1 style='color: gold; font-size: 50px;'>👑 THE QUEEN HAS ARRIVED 👑</h1>
                <div style="font-size: 150px; filter: drop-shadow(0 0 20px #ff9a9e); animation: float 2s ease-in-out infinite;">
                    🎂
                </div>
                <h2 style="color: white; font-family: 'serif';">Make a Wish, Panda! 🌙</h2>
            </div>
        """, unsafe_allow_html=True)

elif page == "Memory Lane":
    st.markdown("<h1 style='text-align:center; color:white;'>📸 Memories</h1>", unsafe_allow_html=True)
    cols = st.columns(3)
    for i in range(1, 7):
        with cols[(i-1)%3]:
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
    items = [("Samba Burgundy", "👟"), ("Lip Gloss", "💄"), ("Panda Plush", "🐼"),
             ("Bouquet", "💐"), ("Designer Outfit", "👗"), ("Mystery Box", "🎁")]
    cols = st.columns(3)
    for idx, (item, icon) in enumerate(items):
        with cols[idx % 3]:
            st.markdown(f"<div class='glass-card'><h2>{icon}</h2><h3>{item}</h3><p style='color:gold;'>FREE</p></div>", unsafe_allow_html=True)
            if st.button(f"Claim {item}", key=idx):
                st.toast(f"{item} reserved! ✨")

elif page == "A Royal Letter":
    pw = st.text_input("Enter Secret Word:", type="password")
    if pw.lower() == "panda":
        st.balloons()
        st.snow()
        
        # Flying Hearts and Balloons
        floating_html = ""
        emojis = ["❤️", "🎈", "💖", "✨"]
        for i in range(15):
            left = i * 6
            delay = i * 0.5
            emoji = emojis[i % len(emojis)]
            floating_html += f'<div class="floating-emoji" style="left:{left}%; animation-delay:{delay}s;">{emoji}</div>'
        st.markdown(floating_html, unsafe_allow_html=True)

        # The Letter (Using unsafe_allow_html=True to show as paragraph)
        st.markdown("""
            <div class="grand-letter">
                <h2 style="color:#d81b60; text-align:center;">To My Best Human</h2>
                <hr>
                <div style="font-size:18px; line-height:1.9; color:#2c3e50;">
                    <p>Many more happy returns to the best one, the cutest, prettiest, boldest, honest, loveliest <b>PANDA</b>... and she who just turned <b>19</b> and is going to have the best days on to come.</p>
                    <p>Always be happy and smiling like the moon smiles (🌙) and whatever happens, <b>Affu</b> has to be brave cuz you're growing from a baby to a woman.</p>
                    <p>Affu will have her best days coming and at this time, you were yelling at me and I'm not talking—sorry for that. But <b>Ashu</b> was a little serious in making you smile on your birthday.</p>
                    <p>There is a set of gifts on the boutique page, so select between them!</p>
                </div>
                <div style="text-align:right; margin-top:40px; border-top: 1px solid #eee; padding-top:10px;">
                    <p style="font-size:22px; font-weight:bold; color:#d81b60;">Once again, Many more happy returns! 🎉🎂❤️</p>
                    <p>— Yours, Ashu</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
