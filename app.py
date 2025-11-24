import streamlit as st
from datetime import date
import base64
import os

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Happy Birthday 🎉",
    page_icon="🎂",
    layout="wide"
)

# =========================================================
# CUSTOM BACKGROUND
# =========================================================
def add_bg(image_file):
    if not os.path.exists(image_file):
        st.error(f"❌ File background '{image_file}' tidak ditemukan.")
        return

    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }}

    /* ANIMASI */
    @keyframes float {{
        0% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-15px); }}
        100% {{ transform: translateY(0px); }}
    }}

    @keyframes fadeIn {{
        0% {{ opacity: 0; }}
        100% {{ opacity: 1; }}
    }}

    @keyframes zoomIn {{
        0% {{ transform: scale(0.5); opacity: 0; }}
        100% {{ transform: scale(1); opacity: 1; }}
    }}

    /* JUDUL */
    .title-glow {{
        animation: float 4s ease-in-out infinite;
        color: #ffb6c1;
        text-shadow: 0px 0px 10px #ff69b4, 0px 0px 20px #ff1493;
        font-family: 'Georgia', serif;
        font-size: 60px;
        text-align: center;
        font-weight: bold;
        margin-top: 20px;
        animation: fadeIn 2s ease-in-out;
    }}

    /* KARTU GLASS */
    .glass {{
        background: rgba(255,255,255,0.25);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255,255,255,0.4);
        box-shadow: 0 4px 20px rgba(0,0,0,0.2);
        animation: zoomIn 1s ease;
    }}

    /* BUTTON */
    .stButton>button {{
        background: linear-gradient(45deg, #ff69b4, #ff1493);
        color: white;
        padding: 12px 20px;
        border-radius: 10px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
        box-shadow: 0px 4px 10px rgba(255,20,147,0.4);
    }}
    .stButton>button:hover {{
        transform: scale(1.05);
        box-shadow: 0px 6px 15px rgba(255,20,147,0.7);
    }}

    /* ANIMASI FOTO */
    .uploaded-img {{
        animation: zoomIn 1s ease-in-out;
    }}

    /* TYPING EFFECT */
    .typing {{
        width: 100%;
        border-right: 3px solid #ff1493;
        white-space: nowrap;
        overflow: hidden;
        animation: typing 4s steps(40, end), blink .6s infinite;
        font-size: 20px;
        font-style: italic;
        color: #333;
    }}
    @keyframes typing {{
        from {{ width: 0 }}
        to {{ width: 100% }}
    }}
    @keyframes blink {{
        50% {{ border-color: transparent }}
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

add_bg("ChatGPT Image 23 Nov 2025, 23.36.36.png")

# =========================================================
# MUSIC PLAYER
# =========================================================
def play_music(audio_file):
    if os.path.exists(audio_file):
        audio_bytes = open(audio_file, "rb").read()
        st.audio(audio_bytes, format="audio/mp3", autoplay=True)

play_music("happybirthday.mp3")

# =========================================================
# MODE OTOMATIS / MANUAL
# =========================================================

st.write("")
mode = st.radio("🌟 Pilih Mode Tampilan:", ["✨ Mode Otomatis", "📝 Mode Manual"])

# Set nilai default (untuk mode otomatis)
default_photo = "background (2).png"   # Ganti dengan foto otomatis Anda
default_ucapan = """
Semoga panjang umur, sehat selalu, banyak rezeki, dan semua impianmu tercapai! ✨🎉
"""
default_tanggal = date(2005, 11, 24)

# =========================================================
# HEADER
# =========================================================
st.markdown("<div class='title-glow'>🎉 Happy Birthday! 🎂</div>", unsafe_allow_html=True)
st.write("")

# =========================================================
# FOTO (OTOMATIS / MANUAL)
# =========================================================
st.subheader("📸 Foto Ulang Tahun", divider="red")

if mode == "✨ Mode Otomatis":
    if os.path.exists(default_photo):
        st.image(default_photo, use_column_width=True)
        st.balloons()
    else:
        st.warning(f"⚠ Foto otomatis '{default_photo}' tidak ditemukan.")

else:
    img = st.file_uploader("Upload foto (opsional)", type=["jpg", "jpeg", "png"])
    if img:
        st.markdown("<div class='uploaded-img'>", unsafe_allow_html=True)
        st.image(img, use_column_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
        st.balloons()

# =========================================================
# UCAPAN SPESIAL
# =========================================================
st.subheader("💌 Ucapan Spesial", divider="red")

if mode == "✨ Mode Otomatis":
    ucapan = default_ucapan
    st.markdown(f"""
    <div class="glass">
        <p class="typing">“{ucapan}”</p>
    </div>
    """, unsafe_allow_html=True)
    st.snow()

else:
    ucapan = st.text_area("Tuliskan ucapan yang indah:", default_ucapan, height=150)
    if st.button("✨ Tampilkan Ucapan"):
        st.markdown(f"""
        <div class="glass">
            <p class="typing">“{ucapan}”</p>
        </div>
        """, unsafe_allow_html=True)
        st.snow()

st.write("---")

# =========================================================
# COUNTDOWN
# =========================================================
st.subheader("📅 Hitung Mundur ke Ulang Tahun", divider="red")

if mode == "✨ Mode Otomatis":
    dob = default_tanggal
else:
    dob = st.date_input("Pilih tanggal ulang tahun:", value=default_tanggal)

today = date.today()
next_birthday = date(today.year, dob.month, dob.day)
if next_birthday < today:
    next_birthday = date(today.year + 1, dob.month, dob.day)

days_left = (next_birthday - today).days
st.info(f"🎯 Tanggal **{days_left} hari** menuju ulang tahun! 🎉")

# =========================================================
# SHARE WHATSAPP
# =========================================================
st.subheader("📲 Share Ke WhatsApp", divider="red")

wa_text = f"Aku mau ngucapin selamat ulang tahun! Ini ucapannya: {default_ucapan if mode=='✨ Mode Otomatis' else ucapan}"
wa_text_encoded = wa_text.replace(" ", "%20").replace("\n", "%0A")
wa_link = f"https://wa.me/?text={wa_text_encoded}"

st.markdown(f"""
<a href="{wa_link}" target="_blank">
    <button style="
        background-color: #25D366;
        color: white;
        border-radius: 10px;
        padding: 12px 20px;
        border: none;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    ">
        Kirim ke WhatsApp
    </button>
</a>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================
st.write("---")
st.caption("✨ Dibuat oleh Aswandy • Streamlit Birthday Aesthetic ✨")
