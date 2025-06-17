# content.py

import streamlit as st
import time

def display_main_content():
    """Menampilkan seluruh konten utama setelah kuis berhasil."""
    st.markdown("<h3 style='text-align: center; color: #ff4081;'>Halo, Nesty, Sang-Segalanya Edwin 💖</h3>", unsafe_allow_html=True)
    st.markdown("""
    <h2 class='main-title'>
        ✨ Sekarang kamu bisa buka semuanya ✨<br>
        Kita selalu mengutuk Purwakarta,<br>
        tapi disinilah kita bisa bertemu<br>
        hingga akhirnya bersama sampai lebih dari Selamanya.
    </h2>
    """, unsafe_allow_html=True)
    st.markdown("""
    <h3 class='sub-title-sidang'>
        🎉 Selamat Sidang 🎉<br>Nesty Ermin Nadhirah <span style='font-weight: bold; color: #e91e63;'>(Unofficially)!</span>✨ S.Pd ✨<br>
        <span>Your hard work shines brightest today!</span>
    </h3>
    """, unsafe_allow_html=True)
    
    with st.expander("💌 Pesan Pertamaku untukmu"):
        st.markdown("""
        Halo, Nesty. Mungkin ini bukan kata-kata yang mudah kuucapkan secara langsung, tapi kuharap ini bisa menyampaikan apa yang ada di hatiku. Sejak awal aku mengenalmu, ada sesuatu yang berbeda. Ada pancaran unik yang membuatku ingin terus belajar tentang dirimu. Aku ingat bagaimana pertama kali mataku terpaku padamu, pada senyummu yang selalu bisa menerangi hariku. Setiap detail kecil tentangmu, dari caramu berbicara hingga tawa renyahmu, semuanya adalah anugerah bagiku. Mungkin ini terdengar klise, tapi kau benar-benar mengubah caraku melihat dunia.
        """)
    with st.expander("👀 Awal Mula Aku Perhatikan Kamu"):
        st.markdown("""
        Nona manis yang kuperhatikan dari jauh: kacamata bulat, gigi gingsul, postur ramping. Awalnya kamu hanya siluet di balik kesibukan, tapi semakin kuperhatikan, semakin nyata kehadiranmu di duniaku. Kita sama-sama PSDO, sama-sama pusing hadapi SK rektor. Kamu PGSD, aku Telekomunikasi. Kamu teladan, aku si pemalas logis. Tapi dari beda itu, kamu jadi magnet semesta kecilku. Kamu memberi warna dalam hidup yang monoton ini. Aku ingat bagaimana kita sering berpapasan di koridor, kadang bertukar senyum singkat, tanpa kusadari bahwa saat-saat itu adalah awal dari sesuatu yang begitu berarti. Setiap kali kau lewat, duniaku seperti sedikit lebih cerah.
        """)
    with st.expander("🌪️ Kita Melawan Dunia"):
        st.markdown("""
        Kita jadi ketua himpunan. Kamu di pendidikan, aku di teknik. Aku pikir kamu akan tenggelam di dunia laki-laki, tapi kamu malah mewarnainya. Kita berdua berdiri melawan fitnah, dari wakil direktur sampai masyarakat palsu. Kamu kehilangan teman, tapi kamu menemukan dirimu. Dan aku menyaksikannya, mencintainya. Ada luka di langkahmu, tapi juga keberanian yang tak pernah kau sadari sendiri. Setiap tantangan yang kita hadapi bersama, setiap rintangan yang kita lewati, hanya membuat ikatan kita semakin kuat. Aku selalu kagum melihatmu bangkit dari setiap badai, bahkan saat aku sendiri merasa ragu.
        """)
    with st.expander("🏆 Saat Kamu Terus Bersinar"):
        st.markdown("""
        Aku kalah pilpres, kamu tetap berdiri. Kamu lolos Kampus Mengajar, MSIB, bahkan jadi Caraka Kamjar. Sementara aku... gagal berkali-kali. Tapi kamu tetap menuntunku dengan cinta. Kamu masak, kamu kerja, kamu skripsi sambil nangis. Bahkan saat PTESOL gagal 5x, kamu bangkit lagi. Kamu nggak tahu betapa kuat kamu dilihat dari mata orang yang cinta padamu. Kamu bukan wanita biasa. Kamu rumah bagi seseorang yang terlalu sering tersesat. Melihatmu berjuang dan meraih setiap impianmu memberiku inspirasi yang tak terhingga. Kamu adalah bukti nyata bahwa ketekunan dan semangat tidak akan pernah mengkhianati hasil. Aku selalu belajar darimu, Nesty. Bahkan lebih dari yang kamu tau.
        """)
    with st.expander("🎓 Hari Ini Kamu Sidang"):
        st.markdown("""
        Aku nggak punya bunga, nggak punya uang, nggak punya hadiah mewah. Tapi aku punya satu hal: Aku menyaksikan semuanya. Dan kamu menang bukan karena kamu pintar, tapi karena kamu bertahan. Hari ini kamu sidang. Tapi bagiku kamu sudah lulus sejak kamu nggak menyerah. Sejak kamu memilih untuk tetap berdiri meski lututmu gemetar. Perjalananmu bukan hanya tentang gelar, Nesty, tapi tentang bagaimana kamu tumbuh dan menjadi pribadi yang luar biasa. Aku bangga, sangat bangga, menjadi bagian dari ceritamu.
        """)
    with st.expander("🌟 Momen-momen Tak Terlupakan Bersamamu"):
        st.markdown("""
        Setiap tawa, setiap canda, setiap obrolan larut malam, semuanya adalah harta bagiku. Momen-momen sederhana seperti saat kita makan di supiak kamba, ke mang eto. Bahkan kalau kamu ingat tempat bersejarah antara kita melawan dunia di dekat Rel itu wkwk. Ya even untuk sekadar menikmati hari bersama, itu semua tak ternilai. Kita selalu mengutuk Purwakarta, tapi disinilah kita bisa bertemu hingga akhirnya bersama sampai lebih dari Selamanya. Aku suka bagaimana kita bisa menjadi diri sendiri saat bersama, tanpa perlu berpura-pura. Kamu adalah ruang aman bagiku, tempat di mana aku bisa jujur tentang segala hal. Terima kasih untuk setiap kenangan indah yang telah kita ciptakan bersama, Nesty. Dan aku berharap akan ada lebih banyak lagi di masa depan.
        """)
    with st.expander("💫 Masa Depan Kita"):
        st.markdown("""
        Aku tahu kita masih punya banyak jalan yang harus dilalui, banyak rintangan yang mungkin akan datang. Tapi satu hal yang aku yakini, aku ingin melaluinya bersamamu. Aku ingin melihatmu terus bersinar, meraih impian-impianmu yang lebih besar lagi. Aku akan selalu ada di sisimu, mendukungmu, menjadi sandaranmu. Biarkan kita terus menulis cerita kita, halaman demi halaman, dengan cinta dan kebersamaan. Aku tidak tahu apa yang akan terjadi esok, tapi bersamamu, aku merasa siap menghadapi apa pun.
        """)

    if st.button("💌 Buka Pesan Rahasia Edwin"):
        with st.spinner("Menyusun kata-kata yang sulit diucapkan..."):
            time.sleep(2)
        st.success("""
        Nesty, Kata bangga, senang, mungkin tidak bisa lagi mewakilkan, tapi satu hal yang ku tau. Gausah pamer sama Dunia yang bahkan nggak tahu usahamu, ke aku aja, seseorang yang selalu berharap jadi Duniamu. Karena aku dan kamu adalah kita, dan kita lebih dari apapun, bahkan melewati waktu itu sendiri. Bahkan sampai kini, aku masih salah tingkah pabila melihat senyum manismu itu. 💖
        """)
    
    st.markdown("""
    <p style='text-align: center; font-size: 16px; margin-top: 30px;'>
    Jangan takut melangkah. Kamu nggak sendiri. Kamu punya dirimu, dan kamu punya aku, selalu 💌<br><br>
    <i>– penuh cinta - Edwin Pujiantoro.</i>
    </p>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<h4 style='text-align: center; color: #ff69b4; margin-top: 40px;'>Album Perjalanan Hebat Nesty 📸</h4>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px;'>Setiap foto ini, adalah bukti nyata dari kegigihan dan semangatmu. Aku saksinya!</p>", unsafe_allow_html=True)
    
    with st.expander("Lihat Semua Momen Perjuangan (Klik di sini!)", expanded=True):
        TOTAL_PHOTOS = 45
        current_index = st.session_state.photo_index

        col1, col2 = st.columns(2)
        with col1:
            if st.button("< Sebelumnya", use_container_width=True):
                st.session_state.photo_index = (current_index - 1 + TOTAL_PHOTOS) % TOTAL_PHOTOS
                st.rerun()
        with col2:
            if st.button("Berikutnya >", use_container_width=True):
                st.session_state.photo_index = (current_index + 1) % TOTAL_PHOTOS
                st.rerun()
        st.markdown("---")

        image_path = f"assets/kenangan ({current_index + 1}).jpg"
        try:
            st.image(image_path, caption=f"Kenangan {current_index + 1} dari {TOTAL_PHOTOS}", use_container_width=True)
        except Exception:
            st.warning(f"File foto '{image_path}' tidak ditemukan.")

    st.markdown("---")
    st.markdown("<h4 style='text-align: center; color: #ff69b4; margin-top: 40px;'>💐 Daripada Buket, Ini Aku Kasih SEKebun-kebunnya! 💐</h4>", unsafe_allow_html=True)
    
    try:
        st.image("assets/kebun_bunga.png", caption="Mungkin ini bukan kebun asli, tapi cintanya lebih luas dari ini, lebih dari waktu 🤍", use_container_width=True)
    except Exception:
        st.warning("File 'assets/kebun_bunga.png' tidak ditemukan.")
    
    st.markdown("""
    <div class='kebun-bunga-closing'>
    Setiap bunga, daun, rumput, pohon, gunung di kebun ini adalah harapan dan rasa bangga yang kutanam untukmu.<br>
    Walau sepertinya ini tidak bisa menggambarkan rasa bangga-ku padamu secara eksplisit dengan hanya satu gambar ini saja.<br>
    Juga tidak akan pernah mampu menggantikan buket bunga nyata atau segala bentuk kemewahan duniawi<br>
    yang mungkin bisa ditawarkan oleh orang lain yang lebih "mampu".<br><br>
    Namun, semoga kamu selalu mekar, seindah dan sekuat kebun bunga<br>
    yang tak lekang oleh waktu, dan kita juga semoga lebih lama daripada "selamanya".<br><br>
    <span class="closing-highlight">Sekali lagi selamat, kesayangan, kepunyaan, segalanya-Edwin,</span>
    <span class="closing-name">Nesty Ermin Nadhirah (Unofficially) S.Pd.</span>
    <span class="closing-final">Tunggu aku, sebentar lagi aku akan menyusulmu, seperti biasa.</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<h4 style='text-align: center; color: #e91e63; margin-top: 40px;'>Kirim Balasan untuk Edwin? 👇</h4>", unsafe_allow_html=True)
    if st.button("💖 Aku Juga Sayang Kamu, Edwin!"):
        st.success("❤️")
        time.sleep(0.5)
        st.success("Aww, pesanmu sudah sampai di hati Edwin! Terima kasih, Nesty! 🥰")
        st.success("❤️")
        time.sleep(2)
        st.info("Pesan ini akan tetap di sini, sama seperti cintaku padamu. 😊")