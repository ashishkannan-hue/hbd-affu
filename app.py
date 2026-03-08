elif page == "A Royal Letter":
    # Custom CSS for flying elements
    st.markdown("""
        <style>
        @keyframes fly-up {
            0% { transform: translateY(100vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(-100vh) rotate(360deg); opacity: 0; }
        }
        .floating-emoji {
            position: fixed;
            bottom: -100px;
            font-size: 24px;
            animation: fly-up 5s linear infinite;
            z-index: 999;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="text-align:center; color:white;">🔐 The Private Vault</h1>', unsafe_allow_html=True)
    pw = st.text_input("Enter Secret Word:", type="password")
    
    if pw.lower() == "panda":
        # 1. Trigger Streamlit's built-in flying effects
        st.balloons()
        st.snow() # Snowflakes look like magical sparkles in this theme
        
        # 2. Add Custom Flying Hearts and Balloons using HTML/CSS
        # We create multiple emojis with different positions and delays
        floating_html = ""
        emojis = ["❤️", "🎈", "💖", "✨", "🌸"]
        for i in range(15):
            left_pos = i * 7  # Spreads them across the screen
            delay = i * 0.5   # Staggers the start time
            emoji = emojis[i % len(emojis)]
            floating_html += f'<div class="floating-emoji" style="left:{left_pos}%; animation-delay:{delay}s;">{emoji}</div>'
        
        st.markdown(floating_html, unsafe_allow_html=True)

        # 3. Your Royal Letter
        st.markdown(f"""
            <div class="grand-letter">
                <h2 style="color:#d81b60; text-align:center;">To My Best Human</h2>
                <hr style="border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0,0,0,0), rgba(212,175,55,0.75), rgba(0,0,0,0));">
                <p style="font-size:18px; line-height:1.9;">
                    Many more happy returns to the best one, the cutest, prettiest, boldest, honest, loveliest <b>PANDA</b>... 
                    and she who just turned <b>19</b> and is going to have the best days on to come.
                </p>
                <p style="font-size:18px; line-height:1.9;">
                    Always be happy and smiling like the moon smiles (🌙) and whatever happens, <b>Affu</b> has to be brave 
                    cuz you're growing from a baby to a woman. 
                </p>
                <p style="font-size:18px; line-height:1.9;">
                    Affu will have her best days coming and at this time, you were yelling at me and I'm not talking—sorry for that. 
                    But <b>Ashu</b> was a little serious in making you smile on your birthday. 
                </p>
                <p style="font-size:18px; line-height:1.9; font-weight: bold; text-align: center; color: #d81b60;">
                    There is a set of gifts on the boutique page, so select between them!
                </p>
                <div style="text-align:right; margin-top:40px;">
                    <p style="font-size:20px; font-weight:bold; color:#d81b60; margin-bottom:0;">
                        Once again, Many more happy returns! 🎉🎂❤️
                    </p>
                    <p style="font-size:18px; color:#555;">— Ashu</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
    elif pw != "":
        st.error("Access Denied. Hint: Your nickname! 🐼")
