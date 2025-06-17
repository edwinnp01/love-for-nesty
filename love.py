import streamlit as st
import time

# ---------------- KONFIGURASI HALAMAN ----------------
st.set_page_config(page_title="Untuk Nesty 💖", page_icon="💌", layout="centered")

# ---------------- SESSION STATE ----------------
if "quiz_attempts" not in st.session_state:
    st.session_state.quiz_attempts = 0
if "quiz_passed" not in st.session_state:
    st.session_state.quiz_passed = False
if "force_pass" not in st.session_state:
    st.session_state.force_pass = False

# ---------------- BACKGROUND WARNA ----------------
st.markdown("""
<style>
body {
    background-color: #fff5f8;
    font-family: 'Helvetica Neue', sans-serif;
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

# ---------------- AUDIO DI AWAL ----------------
st.audio("assets/lagu_nesty.mp3", format="audio/mp3", start_time=0)
st.markdown("<p style='text-align: center; color: #e91e63; font-size: 14px;'>Putar dulu ya, biar makin syahdu 🎶</p>", unsafe_allow_html=True)

# ---------------- EFEK LOPE & JUDUL ----------------
if st.session_state.quiz_attempts == 0 and not st.session_state.quiz_passed:
    st.success("❤️") # Efek lope di awal
    time.sleep(0.5) # Jeda sebentar
    st.markdown("<h2 style='text-align: center; color: #e91e63;'>💘 Untuk Nesty: Perjalanan Cinta & Bangga 💘</h2>", unsafe_allow_html=True)
    st.write("Sebelum kamu buka semua isinya, jawab ini dulu ya!")

# ---------------- QUIZ ----------------
if not st.session_state.quiz_passed and not st.session_state.force_pass:
    st.subheader("💡 Siapa kamu?")
    pilihan = st.radio(
        "Pilih jawaban yang paling benar (menurut Edwin) :",
        ["A. Nesty wanita Edwin", "B. Nesty pacar Edwin", "C. Nesty calon istri Edwin", "D. Nesty paling cantik di dunia"] # All incorrect for a playful twist
    )

    if st.button("Kirim Jawaban"):
        st.session_state.quiz_attempts += 1

        if pilihan == "A. Nesty wanita Edwin" or pilihan == "B. Nesty pacar Edwin" or pilihan == "C. Nesty calon istri Edwin" or pilihan == "D. Nesty paling cantik di dunia":
            if st.session_state.quiz_attempts < 3:
                st.error("Belum benar 😜 Coba lagi ya!")
            else:
                st.warning("Hihihi becandaaa, halo segalanya Edwin 💖")
                st.session_state.quiz_passed = True
                st.session_state.force_pass = True # Force pass after 3 attempts
                time.sleep(1)
        else: # Fallback, though unlikely to be hit
            if st.session_state.quiz_attempts < 3:
                st.error("Belum benar 😜 Coba lagi ya!")
            else:
                st.warning("Hihihi becandaaa, halo segalanya Edwin 💖")
                st.session_state.quiz_passed = True
                st.session_state.force_pass = True
                time.sleep(1)

# ---------------- KONTEN UTAMA ----------------
if st.session_state.quiz_passed or st.session_state.force_pass:
    if st.session_state.quiz_attempts >= 3 and not st.session_state.quiz_passed:
        st.markdown("<h3 style='text-align: center; color: #ff4081;'>Hihihi becandaaa, halo segalanya Edwin 💖</h3>", unsafe_allow_html=True)
    elif st.session_state.quiz_passed and not st.session_state.force_pass:
        st.markdown("<h3 style='text-align: center; color: #ff4081;'>Jawaban Benar! Halo, Nesty, sang kebanggaan Edwin 💖</h3>", unsafe_allow_html=True)

    st.markdown("## ✨ Sekarang kamu bisa buka semuanya ✨")

    with st.expander("💌 Pesan Pertamaku untukmu"):
        st.markdown("""
        Halo, Nesty. Mungkin ini bukan kata-kata yang mudah kuucapkan secara langsung, tapi kuharap ini bisa menyampaikan apa yang ada di hatiku.
        Sejak awal aku mengenalmu, ada sesuatu yang berbeda. Ada pancaran unik yang membuatku ingin terus belajar tentang dirimu.
        Aku ingat bagaimana pertama kali mataku terpaku padamu, pada senyummu yang selalu bisa menerangi hariku.
        Setiap detail kecil tentangmu, dari caramu berbicara hingga tawa renyahmu, semuanya adalah anugerah bagiku.
        Mungkin ini terdengar klise, tapi kau benar-benar mengubah caraku melihat dunia.
        """)

    with st.expander("👀 Awal Mula Aku Perhatikan Kamu"):
        st.markdown("""
        Nona manis yang kuperhatikan dari jauh: kacamata bulat, gigi gingsul, postur ramping.
        Awalnya kamu hanya siluet di balik kesibukan, tapi semakin kuperhatikan, semakin nyata kehadiranmu di duniaku.
        Kita sama-sama PSDKU, sama-sama pusing hadapi SK rektor.
        Kamu PGSD, aku Telekomunikasi. Kamu teladan, aku si pemalas logis.
        Tapi dari beda itu, kamu jadi magnet semesta kecilku. Kamu memberi warna dalam hidup yang monoton ini.
        Aku ingat bagaimana kita sering berpapasan di koridor, kadang bertukar senyum singkat, tanpa kusadari bahwa saat-saat itu adalah awal dari sesuatu yang begitu berarti.
        Setiap kali kau lewat, duniaku seperti sedikit lebih cerah.
        """)

    with st.expander("🌪️ Kita Melawan Dunia"):
        st.markdown("""
        Kita jadi ketua himpunan. Kamu di pendidikan, aku di teknik.
        Aku pikir kamu akan tenggelam di dunia laki-laki, tapi kamu malah mewarnainya.
        Kita berdua berdiri melawan fitnah, dari wakil direktur sampai masyarakat palsu.
        Kamu kehilangan teman, tapi kamu menemukan dirimu.
        Dan aku menyaksikannya, mencintainya. Ada luka di langkahmu, tapi juga keberanian yang tak pernah kau sadari sendiri.
        Setiap tantangan yang kita hadapi bersama, setiap rintangan yang kita lewati, hanya membuat ikatan kita semakin kuat.
        Aku selalu kagum melihatmu bangkit dari setiap badai, bahkan saat aku sendiri merasa ragu.
        """)

    with st.expander("🏆 Saat Kamu Terus Bersinar"):
        st.markdown("""
        Aku kalah pilpres, kamu tetap berdiri. Kamu lolos Kampus Mengajar, MSIB, bahkan jadi Caraka Kamjar.
        Sementara aku... gagal berkali-kali. Tapi kamu tetap menuntunku dengan cinta.
        Kamu masak, kamu kerja, kamu skripsi sambil nangis. Bahkan saat PTESOL gagal 5x, kamu bangkit lagi.
        Kamu nggak tahu betapa kuat kamu dilihat dari mata orang yang cinta padamu.
        Kamu bukan wanita biasa. Kamu rumah bagi seseorang yang terlalu sering tersesat.
        Melihatmu berjuang dan meraih setiap impianmu memberiku inspirasi yang tak terhingga.
        Kamu adalah bukti nyata bahwa ketekunan dan semangat tidak akan pernah mengkhianati hasil.
        Aku selalu belajar darimu, Nesty.
        """)

    with st.expander("🎓 Hari Ini Kamu Sidang"):
        st.markdown("""
        Aku nggak punya bunga, nggak punya uang, nggak punya hadiah mewah. Tapi aku punya satu hal:
        Aku menyaksikan semuanya. Dan kamu menang bukan karena kamu pintar, tapi karena kamu bertahan.
        Hari ini kamu sidang. Tapi bagiku kamu sudah lulus sejak kamu nggak menyerah. Sejak kamu memilih untuk tetap berdiri meski lututmu gemetar.
        Perjalananmu bukan hanya tentang gelar, Nesty, tapi tentang bagaimana kamu tumbuh dan menjadi pribadi yang luar biasa.
        Aku bangga, sangat bangga, menjadi bagian dari ceritamu.
        """)

    with st.expander("🌟 Momen-momen Tak Terlupakan Bersamamu"):
        st.markdown("""
        Setiap tawa, setiap canda, setiap obrolan larut malam, semuanya adalah harta bagiku.
        Momen-momen sederhana seperti saat kita berbagi es krim favorit atau sekadar menikmati senja bersama, itu semua tak ternilai.
        Aku suka bagaimana kita bisa menjadi diri sendiri saat bersama, tanpa perlu berpura-pura.
        Kamu adalah ruang aman bagiku, tempat di mana aku bisa jujur tentang segala hal.
        Terima kasih untuk setiap kenangan indah yang telah kita ciptakan bersama, Nesty.
        Dan aku berharap akan ada lebih banyak lagi di masa depan.
        """)

    with st.expander("💫 Masa Depan Kita"):
        st.markdown("""
        Aku tahu kita masih punya banyak jalan yang harus dilalui, banyak rintangan yang mungkin akan datang.
        Tapi satu hal yang aku yakini, aku ingin melaluinya bersamamu.
        Aku ingin melihatmu terus bersinar, meraih impian-impianmu yang lebih besar lagi.
        Aku akan selalu ada di sisimu, mendukungmu, menjadi sandaranmu.
        Biarkan kita terus menulis cerita kita, halaman demi halaman, dengan cinta dan kebersamaan.
        Aku tidak tahu apa yang akan terjadi esok, tapi bersamamu, aku merasa siap menghadapi apa pun.
        """)

    if st.button("💌 Buka Pesan Rahasia Edwin"):
        with st.spinner("Menyusun kata-kata yang sulit diucapkan..."):
            time.sleep(2)
        st.success("Nesty, aku bangga banget sama kamu. Gausah pamer sama Dunia yang bahkan nggak tahu usahamu, ke aku aja yaitu seseorang yang selalu berharap jadi 'Duniamu' 💖")

    st.markdown("""
    <p style='text-align: center; font-size: 16px; margin-top: 30px;'>
    Jangan takut melangkah. Kamu nggak sendiri. Kamu punya dirimu, dan kamu punya aku, selalu 💌<br><br>
    <i>– penuh cinta - Edwin Pujiantoro.</i>
    </p>
    """, unsafe_allow_html=True)



    # ---------------- ALBUM PERJUANGAN HEBAT NESTY 📸 ----------------
    st.markdown("<h4 style='text-align: center; color: #ff69b4; margin-top: 40px;'>Album Perjalanan Hebat Nesty 📸</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px;'>Setiap foto ini, adalah bukti nyata dari kegigihan dan semangatmu. Aku saksinya!</p>", unsafe_allow_html=True)

    with st.expander("Lihat Semua Momen Perjuangan (Klik di sini!)"):
        for i in range(1, 46): # Loop dari 1 sampai 45
            image_path = f"assets/kenangan ({i}).jpg" # Pastikan ekstensi file sesuai (.png, .jpg, dll.)
            try:
                st.image(image_path, caption=f"Momen Perjuangan ke-{i} ✨", use_container_width=True)
                time.sleep(0.1) # Jeda sedikit agar tidak terlalu cepat
            except FileNotFoundError:
                st.warning(f"File foto '{image_path}' tidak ditemukan. Pastikan nama dan ekstensi file sudah benar.")


    # ---------------- KEBUN BUNGA DIGITAL ----------------
    st.markdown("<h4 style='text-align: center; color: #ff69b4; margin-top: 40px;'>💐 Daripada Buket, Ini Aku Kasih SEKebun-kebunnya! 💐</h4>", unsafe_allow_html=True)

    # Menggunakan gambar kebun bunga lokal
    st.image("assets/kebun_bunga.png", # <--- Pastikan path dan nama file benar
              caption="Mungkin ini bukan kebun asli, tapi cintanya lebih luas dari ini, lebih dari waktu 💗",
              use_container_width=True)

    st.markdown("""
    <div style='text-align: center;'>
    Setiap bunga di kebun ini adalah harapan dan rasa bangga yang kutanam untukmu (ga sesedikit yang digambar ya njir wkwk).<br>
    Semoga kamu selalu mekar, seindah dan sekuat kebun bunga yang tak lekang oleh waktu dan kita juga semoga lebih lama daripada "selamanya".
    </div>
    """, unsafe_allow_html=True)

    
    # --- TOMBOL BALASAN DARI NESTY ---
    st.markdown("<h4 style='text-align: center; color: #e91e63; margin-top: 40px;'>Kirim Balasan untuk Edwin? 👇</h4>", unsafe_allow_html=True)
    if st.button("💖 Aku Juga Sayang Kamu, Edwin!"):
        st.success("❤️") # Efek lope sebagai respons
        time.sleep(0.5)
        st.success("Aww, pesanmu sudah sampai di hati Edwin! Terima kasih, Nesty! 🥰")
        st.success("❤️") # Efek lope lagi
        time.sleep(2)
        st.info("Pesan ini akan tetap di sini, sama seperti cintaku padamu. 😊")