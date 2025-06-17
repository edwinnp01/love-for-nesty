# love.py (File Utama)

import streamlit as st
import time
# Import data dan fungsi dari file lain
from quiz_data import QUIZ_DATA
from content import display_main_content

# ---------------- KONFIGURASI HALAMAN ----------------
st.set_page_config(page_title="Untuk Nesty 💖", page_icon="💌", layout="centered")

# ---------------- SESSION STATE ----------------
def init_session_state():
    """Menginisialisasi semua state yang dibutuhkan untuk alur aplikasi."""
    if "page" not in st.session_state:
        st.session_state.page = "start"
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "photo_index" not in st.session_state:
        st.session_state.photo_index = 0
    for q in QUIZ_DATA:
        if "secret_key" in q and q["secret_key"] not in st.session_state:
            st.session_state[q["secret_key"]] = False

init_session_state()

# ---------------- FUNGSI KALKULASI SKOR ----------------
def calculate_score():
    """Menghitung skor akhir dari jawaban yang tersimpan."""
    answers = st.session_state.answers
    score = 0
    for question_data in QUIZ_DATA:
        q_key = f"q{question_data['q_num']}"
        correct_answer = question_data["correct_answer"]
        if question_data.get("type", "radio") == "text":
            if answers.get(q_key, "").strip() != "":
                score += 1
        else:
            if answers.get(q_key) == correct_answer:
                score += 1
    st.session_state.score = score
    st.session_state.page = "results"
    st.rerun()

# ---------------- ALUR UTAMA APLIKASI (ROUTER) ----------------

# Tampilkan CSS & Audio di setiap halaman
st.markdown("""
<style>
body { background-color: #fff5f8; font-family: 'Helvetica Neue', sans-serif; color: #333333; }
.main-title { text-align: center !important; color: #e91e63; font-size: 2.2em; margin-bottom: 25px; }
.sub-title-sidang { text-align: center !important; color: #58a6ff; font-size: 1.8em; margin-top: 30px; margin-bottom: 20px; line-height: 1.3; }
.sub-title-sidang span { font-size: 0.7em; color: #6c757d; display: block; margin-top: 5px; }
.stExpander { margin-bottom: 10px; }
.kebun-bunga-closing { text-align: center; font-size: 1.1em; margin-top: 20px; line-height: 1.6; }
.closing-highlight, .closing-name, .closing-final { display: block; margin-top: 2px; margin-bottom: 2px; }
.closing-highlight { color: #e91e63; font-weight: bold; }
.closing-name { color: #ff69b4; font-weight: bold; }
.closing-final { color: #333333; font-size: 0.9em; margin-top: 5px; }
</style>
""", unsafe_allow_html=True)

try:
    st.audio("assets/lagu_nesty.mp3", format="audio/mp3", start_time=0)
    st.markdown("<p style='text-align: center; color: #e91e63; font-size: 14px;'>Putar dulu ya ini ya manis, biar makin syahdu 🎶</p>", unsafe_allow_html=True)
    with st.expander("Kenapa lagu ini?"):
        st.markdown("""
        Aku bukan tipe orang yang punya 'lagu favorit', itu konsep yang tidak logis.
        
        Tapi, jika harus ada justifikasi rasional, lagu ini secara efisien selalu memicu satu *output* yang sama: ingatan tentang senyummu. Senyum yang entah kenapa menjadi satu-satunya variabel yang bisa men-debug kehidupanku yang penuh *error* ini, tidak peduli cuacanya sedang hujan atau badai.
        
        Mungkin ini hanya delusi seorang penyendiri. Tapi kalau delusi ini membuat segalanya sedikit lebih baik, kurasa aku tidak akan mempermasalahkannya.
        """)
except Exception:
    st.warning("File audio 'assets/lagu_nesty.mp3' tidak ditemukan.")

# --- Router Halaman ---
if st.session_state.page == "start":
    st.success("❤️")
    st.markdown("<h2 style='text-align: center; color: #e91e63;'>💘 Untuk Nesty 💘<br>Perjalanan Cinta & Bangga-ku Padanya</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Sebelum kamu buka semua isinya, ada kuis pemanasan dulu ya!</p>", unsafe_allow_html=True)
    if st.button("Mulai Kuis Pemanasan!", type="primary"):
        placeholder = st.empty()
        with placeholder.container():
            with st.spinner("Siap-siap..."):
                time.sleep(1)
            for i in range(3, 0, -1):
                st.markdown(f"<h3 style='text-align: center;'>{i}...</h3>", unsafe_allow_html=True)
                time.sleep(1)
            placeholder.empty()
        st.session_state.page = "quiz_1"
        st.rerun()

elif "quiz" in st.session_state.page:
    st.title("💘 Kuis Interaktif Buat Nesty")
    q_num = int(st.session_state.page.split("_")[1])
    st.progress(q_num / len(QUIZ_DATA), text=f"Pertanyaan {q_num} dari {len(QUIZ_DATA)}")
    st.markdown("---")

    question = QUIZ_DATA[q_num - 1]
    q_key = f"q{q_num}"
    st.subheader(f"{question['title']}")

    if question.get("type", "radio") == "text":
        answer = st.text_input("Tulis jawabanmu di sini:", key=f"widget_{q_key}", label_visibility="collapsed")
        st.session_state.answers[q_key] = answer
    else:
        options = question["options"][:]
        if question.get("secret_key") and st.session_state[question["secret_key"]]:
            if question["correct_answer"] not in options:
                options.append(question["correct_answer"])
        answer = st.radio("Pilihan:", options, key=f"widget_{q_key}", label_visibility="collapsed")
        st.session_state.answers[q_key] = answer

    can_proceed = True
    secret_key = question.get("secret_key")
    if secret_key and not st.session_state[secret_key]:
        can_proceed = False
        if st.button(question["secret_button_text"], key=f"reveal_{q_key}"):
            st.session_state[secret_key] = True
            st.rerun()
    if question.get("type") == "text" and not answer.strip():
        can_proceed = False

    if can_proceed:
        st.markdown("---")
        if q_num < len(QUIZ_DATA):
            if st.button("Lanjut ➡️", key=f"next_{q_key}"):
                with st.spinner("Menyiapkan pertanyaan berikutnya..."):
                    time.sleep(0.5)
                    st.session_state.page = f"quiz_{q_num + 1}"
                    st.rerun()
        else:
            if st.button("Lihat Hasil & Buka Surat Cinta!", type="primary"):
                calculate_score()

elif st.session_state.page == "results":
    st.balloons()
    score = st.session_state.score
    st.markdown(f"## 🧾 Skor Akhir Kamu: **{score}/5**")
    if score == 5:
        st.success("Kamu lulus 100%! Kamu emang segalanya bagi Edwin 😍💍.")
        if st.button("Buka Harta Karun! ✨", type="primary"):
            st.session_state.page = "final_content"
            st.rerun()
    else:
        if score >= 3:
            st.info(f"Hampir Sempurna ({score}/5)! Kamu Detektif Cinta Sejati 🕵️‍♀️💕. Tinggal sedikit lagi!")
        else:
            st.warning(f"Skormu {score}/5. Sepertinya ada beberapa rahasia yang masih kusimpan 😉. Ayo coba lagi!")
        if st.button("Ulangi Kuis dari Awal"):
            st.session_state.page = "start"
            st.session_state.answers = {}
            st.session_state.score = 0
            for q in QUIZ_DATA:
                if "secret_key" in q:
                    st.session_state[q["secret_key"]] = False
            st.rerun()

elif st.session_state.page == "final_content":
    display_main_content()
