import streamlit as st
import time
from datetime import datetime
from PIL import Image

# --- PAGE SETUP ---
st.set_page_config(page_title="HBD AFFU 🌙", page_icon="🐼", layout="centered")

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%); }
    .nickname { font-family: 'Arial Black'; color: white; font-size: 60px; text-align: center; text-shadow: 3px 3px 10px rgba(0,0,0,0.3); margin-bottom:0;}
    .sub-text { text-align: center; color: #6a1b9a; font-size: 18px; margin-top: -10px; font-weight: 500; }
    
    /* Letter Styling */
    .letter-container {
        background: #fffdf5;
        padding: 40px;
        border-radius: 5px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border: 1px solid #e0e0e0;
        font-family: 'Georgia', serif;
        color: #333;
        line-height: 1.8;
        position: relative;
    }
    .letter-header { font-size: 24px; color: #d81b60; font-weight: bold; margin-bottom: 20px; border-bottom: 1px solid #ffcfdf; }
    .letter-footer { text-align: right; margin-top: 30px; font-weight: bold; color: #d81b60; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🎈 Affu's 19th Birthday")
page = st.sidebar.radio("Go to:", ["Home & Countdown", "Photo Gallery", "Select Your Gifts", "A Letter for You"])

# --- PAGE 1: HOME & COUNTDOWN ---
if page == "Home & Countdown":
    st.markdown('<p class="nickname">AFFU</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Welcome to your 19th Birthday Hub! ✨</p>', unsafe_allow_html=True)
    
    target_date = datetime(2026, 3, 22, 0, 0, 0)
    countdown_placeholder = st.empty()
    
    while True:
        now = datetime.now()
        diff = target_date - now
        if diff.total_seconds() <= 0:
            countdown_placeholder.success("🎉 HAPPY 19th BIRTHDAY AFFU! 🎉")
            st.balloons()
            break
        days, hours, remainder = diff.days, diff.seconds // 3600, diff.seconds % 3600
        mins, secs = remainder // 60, remainder % 60
        countdown_placeholder.metric("Time until you turn 19... 🌙", f"{days}d {hours}h {mins}m {secs}s")
        time.sleep(1)

# --- PAGE 2: PHOTO GALLERY ---
elif page == "Photo Gallery":
    st.markdown('<h2 style="text-align:center; color:white;">📸 Our Memories</h2>', unsafe_allow_html=True)
    cols = st.columns(2)
    for i in range(1, 5):
        with cols[(i-1)%2]:
            try:
                img = Image.open(f"photo{i}.jpg")
                st.image(img, use_container_width=True, caption=f"Memory #{i}")
            except:
                st.image(f"https://via.placeholder.com/400x450?text=Photo+{i}")

# --- PAGE 3: GIFT SELECTION ---
elif page == "Select Your Gifts":
    st.markdown('<h2 style="text-align:center; color:white;">🎁 Pick Your Surprise!</h2>', unsafe_allow_html=True)
    st.write("I know things were a bit tense, but Ashu was serious about making you smile. Pick your favorites:")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💝 Option A: Chocolate & Flowers"):
            st.success("Sweetness for the sweetest human! ✅")
        if st.button("🧸 Option B: Panda Plushie"):
            st.success("A panda for my favorite Panda! ✅")
    with col2:
        if st.button("👗 Option C: New Outfit"):
            st.success("You'll look stunning! ✅")
        if st.button("✨ Option D: Mystery Surprise"):
            st.warning("Patience is a virtue... ✅")

# --- PAGE 4: A LETTER FOR YOU ---
elif page == "A Letter for You":
    st.subheader("🔐 Locked for Affu")
    pw = st.text_input("Enter the secret word (Hint: Your nickname):", type="password")
    
    if pw.lower() == "panda":
        st.balloons()
        st.markdown(f"""
            <div class="letter-container">
                <div class="letter-header">To My Best Human,</div>
                <p>Many more happy returns to the best one, the cutest, prettiest, boldest, honest, loveliest <b>PANDA</b>..</p>
                <p>She who just turned <b>19</b> and is going to have the best days to come. Always be happy and smiling like the moon smiles (🌙) and whatever happens, Affu has to be brave cuz you're growing from a baby to a woman.</p>
                <p>Affu will have her best days coming and at this time, you were yelling at me and I'm not talking—sorry for that. But Ashu was a little serious in making you smile on your birthday.</p>
                <p>There is a set of gifts on the other page, so select between them!</p>
                <div class="letter-footer">
                    Once again, Many more happy returns of the day to the best HUMAN of my life! 🎉🎂❤️<br>
                    — Ashu
                </div>
            </div>
        """, unsafe_allow_html=True)
    elif pw:
        st.error("That's not the word! Think Panda. 😉")