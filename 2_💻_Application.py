import streamlit as st
from streamlit_option_menu import option_menu

st. markdown("<h1 style='text-align: center; color: white;'>APLIKASI PENGHITUNG LUAS BANGUN DUA DIMENSI DAN TIGA DIMENSI</h1>",  unsafe_allow_html=True)
st.write("---")
st.write("###")

with st.sidebar :
    selected  = option_menu ('HITUNG LUAS BANGUN RUANG',
    ['hitung luas persegi panjang',
     'hitung luas segitiga',
     'hitung luas persegi',
     'hitung luas jajar genjang',
     'hitung luas lingkaran',
     'hitung luas trapesium',
     'hitung luas layang-layang',
     'hitung luas belah ketupat',
     'hitung luas permukaan kubus',
     'hitung luas permukaan balok',
     'hitung luas permukaan bola',],                
    default_index=0,)
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2015/12/01/15/43/black-1072366_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url();

if (selected == 'hitung luas persegi panjang') :
    
    st.subheader("Definisi Persegi Panjang")
    st.write("Persegi panjang merupakan salah satu bangun datar segiempat yang memiliki dua pasang sisi sejajar serta keempat sudutnya merupakan sudut siku-siku.")
    
    from PIL import Image
    image = Image.open('PPJ1.jpg')
    st.image(image, caption='Gambar persegi panjang ABCD')
    
    st.subheader ("Sifat-Sifat Persegi Panjang")
    from PIL import Image
    image = Image.open('PPJ2.jpg')
    st.image(image, caption='Gambar Ilustrasi Sifat-Sifat persegi panjang ABCD')
    st.write (
        """
        - Memiliki empat buah sisi. Dalam persegi panjang ABCD tersebut terdapat empat sisi yaitu sisi AB, BC, CD, dan DA.
        - Sisi-sisi yang sejajar dan berhadapan sama panjang. Dalam persegi panjang ABCD, sisi-sisi yang sejajar dan berhadapan adalah sisi AB dengan sisi CD  dan sisi BC dengan sisi AD.
        - Memiliki dua diagonal yang sama panjang. Dalam persegi panjang di atas terdapat diagonal AC dan diagonal BD. Kedua diagonal memiliki ukuran yang sama.
        - Memiliki empat sudut siku-siku. Dalam persegi panjang ABCD, terdapat sudut ABC, sudut BCD, sudut CDA, dan sudut DAB yang masing-masing berukuran 90o atau sudut siku-siku.
        - Memiliki dua simetri lipat dan simetri putar.
        """)
    st.write("---")
    from PIL import Image
    image = Image.open('PPJ3.jpg')
    st.image(image, caption='Rumus keliling Persegi Panjang')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PPJ4.jpg')
    st.image(image, caption='Rumus Luas Persegi Panjang')
    
    st.markdown("### Hitung Luas Bangun Persegi Panjang")
    panjang = st.number_input("Masukan nilai panjang")
    lebar = st.number_input("Masukan nilai lebar")
    hitung= st.button ("Hitung luas")

    if hitung :
        luas = panjang*lebar
        st.write ("Diperoleh luas persegi panjang adalah ", luas)
        st.success (f"Kesimpulan : luas bangun persegi panjang dengan panjang {panjang} cm dan lebar {lebar} cm adalah {luas} cm2")
        st.snow()
    
        
if (selected == 'hitung luas segitiga') :
    
    st.subheader("Definisi Segitiga")
    st.write("Segitiga merupakan bangun datar yang dibatasi oleh tiga sisi yang mana setiap sisinya memiliki panjang yang sama ataupun berbeda.")
    
    from PIL import Image
    image = Image.open('PSG1.jpg')
    st.image(image, caption='Gambar Jenis-Jenis Segitiga')
    
    st.subheader ("Ciri-ciri segitiga secara umum ")
    st.write (
        """
        - Memiliki tiga sudut yang sama besarnya, yakni 60 derajat. 
        - Memiliki tiga sumbu simetri lipat. 
        - Memiliki tiga sumbu simetri putar.
        """)
    st.write("---")
    from PIL import Image
    image = Image.open('PSG2.jpg')
    st.image(image, caption='Rumus keliling Segitiga')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PSG3.jpg')
    st.image(image, width=600,caption='Rumus Luas Segitiga')
    st.write("##")
    st.write("---")
    st.title ('Hitung Luas Bangun Segitiga')
    
    alas = st.number_input("Masukan ukuran alas")
    tinggi = st.number_input("Masukan ukuran tinggi")
    hitung = st.button ("Hitung luas")
    
    if hitung :
        luas = 0.5* alas* tinggi
        st.write("Diperoleh Luas segitiga adalah ", luas)
        st.success (f"Kesimpulan : Luas segitiga dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas} cm2")
        st.balloons()
        
if (selected == 'hitung luas persegi') :
    st.subheader("Definisi Persegi")
    st.write("Persegi merupakan bentuk bangun datar yang memiliki 4 sisi sama panjang dan semua sudut sudutnya sama besar dan siku-siku serta setiap diagonalnya tegak lurus.") 
    
    st.subheader ("Sifat-Sifat Persegi")
    from PIL import Image
    image = Image.open('PPP1.jpg')
    st.image(image, caption='Gambar Ilustrasi Sifat-Sifat Persegi ABCD')
    st.write (
        """
        - Memiliki 4 sisi sama panjang
        - Setiap sudut yang terbentuk oleh sisinya merupakan sudut siku-siku
        - Setiap diagonalnya membagi 2 sama besar sudut yang terbentuk oleh sisinya
        - Perpotongan antar diagonalnya membentuk sudut siku-siku
        """)

    st.write("---")
    from PIL import Image
    image = Image.open('PPP2.jpg')
    st.image(image, caption='Rumus keliling Persegi')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PPP3.jpg')
    st.image(image, caption='Rumus Luas Persegi')
    st.write("---")
    
    st.title ('Hitung Luas Bangun Persegi')
    sisi = st.number_input ("Masukan ukuran sisi")
    hitung = st.button ("Hitung luas")
    
    if hitung :
        luas = sisi*sisi
        st.write ("luas persegi adalah ", luas)
        st.success (f"Kesimpulan : luas persegi sesuai dengan ukuran sisi {sisi} cm adalah {luas} cm2")
        st.snow()
        
if (selected == 'hitung luas jajar genjang') :
    st.subheader("Definisi Jajar genjang")
    st.write("jajar genjang adalah bangun datar dua dimensi yang dibentuk dari dua pasang rusuk serta masing-masing memiliki panjang yang sama serta saling berhadapan. ")
    
    from PIL import Image
    image = Image.open('PJG1.jpg')
    st.image(image, caption='Gambar Jajar Genjang')
    
    st.subheader ("Sifat-Sifat Jajar Genjang")
    st.write (
        """
        - Memiliki Sisi Sejajar dengan Panjang yang Sama
        - Sudut yang Berhadapan Sama Besar
        - Memiliki Sudut yang Saling Berpelurus
        - Memiliki Diagonal Pembagi
        - Adanya Diagonal yang Saling Berpotongan
        - Memiliki Jumlah Sudut 360 Derajat
        - Tidak Memiliki Sumbu Simetri
        """)
    st.write("---")
    from PIL import Image
    image = Image.open('PJG2.jpg')
    st.image(image, caption='Rumus keliling Jajar Genjang')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PJG3.jpg')
    st.image(image, width=478, caption='Rumus Luas Jajar Genjang')
    
    st.write("---")
    st.title ('Hitung Luas Bangun jajar genjang')
    
    alas = st.number_input("Masukan ukuran alas")
    tinggi = st.number_input("Masukan ukuran tinggi")
    hitung = st.button ("Hitung luas")

    if hitung :
        luas = alas* tinggi
        st.write("Diperoleh luas jajar genjang adalah ", luas)
        st.success (f"Kesimpulan : luas jajar genjang dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas} cm2")
        st.balloons()
        
if (selected == 'hitung luas lingkaran') :
    st.subheader("Definisi Lingkaran")
    st.write("Lingkaran merupakan himpunan titik-titik yang berjarak sama terhadap suatu titik tertentu. Titik tertentu pada lingkaran tersebut disebut sebagai pusat lingkaran. ")
    
    from PIL import Image
    image = Image.open('PL1.jpg')
    st.image(image, width=638, caption='Gambar Detail Lingkaran')
    
    st.subheader ("Sifat-Sifat Lingkaran")
    st.write (
        """
        - Memiliki sebuah titik pusat
        - Memiliki satu buah sisi
        - Tidak memiliki titik sudut
        - Jumlah sudutnya adalah 360°
        - Memiliki simetri lipat tak hingga
        - Memiliki simetri putar tak hingga
        - Memiliki jari-jari dan diameter
        - Memiliki luas dan keliling
        """)
    st.write("---")
    from PIL import Image
    image = Image.open('PL2.jpg')
    st.image(image, width=638, caption='Rumus keliling Lingkaran')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PL3.jpg')
    st.image(image, width=638, caption='Rumus Luas Lingkaran')
    
    st.write("---")
    st.title ('Hitung Luas Bangun lingkaran')
    
    st.text("JIKA DIKETAHUI DIAMETER MAKA : ")
    d = st.number_input ("masukan ukuran diameter")
    hitung = st.button ("Hitung luas")
        
    if hitung :
        r = 0.5*d
        luas =  3.14*r*r
        st.write("Diperoleh luas lingkaran adalah ", luas)
        st.success (f"Kesimpulan : luas lingkaran dengan diameter {d} cm atau jari-jari {r} cm adalah {luas} cm2")
        st.snow()
        
    st.text ("JIKA DIKETAHUI JARI-JARI LINGKARAN MAKA : ")  
    r = st.number_input("Masukan jari-jari lingkaran")
    hitung = st.button ("Hitung luas dengan jari-jari")
    
    if hitung :
        d = 2*r
        luas = 3.14*r*r
        st.write ("Diperoleh luas lingkaran dengan jari-jari di atas adalah", luas )
        st.success(f"kesimpulan : luas lingkaran dengan jari-jari {r} cm atau diameter {d} cm adalah {luas} cm2")
        st.balloons()
        
        
if (selected == 'hitung luas trapesium') :
    st.subheader("Definisi Trapesium")
    st.write("Trapesium adalah segi empat yang mempunyai sepasang sisi yang tepat berhadapan dan sejajar.")
    
    from PIL import Image
    image = Image.open('PT1.jpg')
    st.image(image, caption='Gambar Trapesium')
    
    st.subheader ("Ciri Ciri Trapesium")
    st.write (
        """
        - Jumlah sudutnya berdekatan 180°. 
        - Memiliki sepasang sisi sejajar. 
        - Salah satu kakinya tegak lurus (trapesium siku-siku) terhadap sisi sejajarnya. 
        - Hanya memiliki 1 simetri putar saja Terdapat 4 rusuk dan 4 titik siku
        """)
    st.write("---")
    from PIL import Image
    image = Image.open('PT2.jpg')
    st.image(image, caption='Rumus keliling dan Luas Trapesium')
    
    st.write("---")
    st.title ('Hitung Luas Bangun Trapesium')
    
    atas = st.number_input ("Masukan ukuran sisi sejajar atas")
    bawah = st.number_input ("Masukan ukuran sisi sejajar bawah")
    tinggi = st.number_input ("Masukan tinggi trapesium")
    hitung = st.button ("Hitung luas")
    
    if hitung :
        luas = 0.5*(atas+bawah)*tinggi
        st.write ("luas trapesium adalah ", luas)
        st.success (f"Kesimpulan : luas trapesium sesuai dengan ukuran sisi sejajar atas {atas} cm, sisi sejajar bawah {bawah} cm dan tinggi {tinggi} cm adalah {luas} cm2")
        st.snow()
        
if (selected == 'hitung luas layang-layang') :
    st.subheader("Definisi Layang-Layang")
    st.write("Layang-layang adalah bentuk segiempat yang memiliki dua pasang sisi bersentuhan dan sama panjang. Layang-layang adalah suatu bentuk datar (bentuk dua dimensi) yang terdiri dari dua pasang sisi yang masing-masing memiliki panjang yang sama dan bersudut satu sama lain.")
    
    from PIL import Image
    image = Image.open('PLL1.jpg')
    st.image(image, caption='Gambar Layang-Layang dan Sifat-sifatnya')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PLL2.jpg')
    st.image(image, caption='Rumus keliling dan Luas Layang-Layang')
    
    st.write("---")
    st.title ('Hitung Luas Bangun Layang-Layang')
    
    d1 = st.number_input ("Masukan ukuran diagonal 1")
    d2 = st.number_input ("Masukan ukuran diagonal 2")
    hitung = st.button ("Hitung luas")
    
    if hitung :
        luas = 0.5*d1*d2
        st.write ("luas bangun layang-layang adalah ", luas)
        st.success (f"Kesimpulan : luas bangun layang-layang sesuai dengan ukuran diagonal satu : {d1} cm dan diagonal dua : {d2} cm adalah {luas} cm2")
        st.balloons()
        
if (selected == 'hitung luas belah ketupat') :
    st.subheader("Definisi Belah Ketupat")
    st.write("Belah ketupat adalah bangun datar yang memiliki empat sisi yang sama panjang dengan sisi-sisi yang berhadapan saling sejajar dan tidak saling tegak lurus.")
    
    from PIL import Image
    image = Image.open('PBK1.jpg')
    st.image(image, caption='Gambar Belah Ketupat dan Sifat-sifatnya')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PBK2.jpg')
    st.image(image, caption='Rumus keliling dan Luas Belah Ketupat')
    
    st.write("---")
    st.title ('Hitung Luas Bangun Belah Ketupat')
    
    d1 = st.number_input ("Masukan ukuran diagonal 1")
    d2 = st.number_input ("Masukan ukuran diagonal 2")
    hitung = st.button ("Hitung luas")
    
    if hitung :
        luas = 0.5*d1*d2
        st.write ("luas bangun belah ketupat adalah ", luas)
        st.success (f"Kesimpulan : luas bangun belah ketupat sesuai dengan ukuran diagonal satu : {d1} cm dan diagonal dua : {d2} cm adalah {luas} cm2")
        st.balloons()

  
if (selected == 'hitung luas permukaan kubus') :
    st.subheader("Definisi Kubus")
    st.write("Kubus ialah merupakan bentuk bangun ruang tiga dimensi yang di batasi dengan enam bidang kongruen yang berbentuk bujur sangkar atau persegi.")
    
    from PIL import Image
    image = Image.open('PK1.jpg')
    st.image(image, caption='Gambar Kubus dan Ciri-Cirinya')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PK2.jpg')
    st.image(image, caption='Rumus Luas Permukaan dan Volume Kubus')
    
    st.write("---")
    st.title ('Hitung Luas Permukaan Kubus')

    sisi = st.number_input("Masukan ukuran sisi kubus (cm)")
    hitung = st.button("hitung Luas Permukaan")

    if hitung :
        LP = 6*(sisi*sisi)
        st.write ("Diperoleh luas permukaan kubus adalah",LP)
        st.success (f"Kesimpulan : luas permukaan kubus dengan sisi {sisi} cm adalah {LP} cm3")
        st.snow()
        
if (selected == 'hitung luas permukaan balok') :
    st.subheader("Definisi Balok")
    st.write("Balok merupakan bangun ruang yang dibatasi oleh tiga pasang sisi sejajar yang berbentuk persegi atau persegi panjang dengan setidaknya terdapat satu pasang sisi sejajar yang memiliki ukuran yang berbeda.")
    
    st.write("---")
    st.subheader("Ciri-Ciri Balok")
    from PIL import Image
    image = Image.open('PB1.jpg')
    st.image(image, caption='Gambar Balok dan Ciri-Cirinya')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PB2.jpg')
    st.image(image, caption='Rumus Luas Permukaan Balok')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PB3.jpg')
    st.image(image, caption='Rumus Volume Balok')
    
    st.write("---")
    st.title ('Hitung Luas Permukaan Balok')

    panjang = st.number_input("Masukan ukuran panjang balok (cm)")
    lebar = st.number_input ("Masukan ukuran lebar balok (cm)")
    tinggi = st.number_input ("Masukan ukuran tinggi balok (cm)")
    hitung = st.button("hitung Luas Permukaan")

    if hitung :
        LP = 2*(panjang*lebar+panjang*tinggi+lebar*tinggi)
        st.write ("Diperoleh luas permukaan balok adalah",LP)
        st.success (f"Kesimpulan : luas permukaan balok dengan panjang {panjang} cm, lebar {lebar} cm, tinggi {tinggi} cm adalah {LP} cm3")
        st.balloons()


if (selected == 'hitung luas permukaan bola') :
    st.subheader("Definisi Bola")
    st.write("Bola yaitu bangun ruang sisi lengkung yang dibatasi oleh sebuah bidang lengkung. Sebuah bangun ruang bola, bisa dibentuk dari setengah lingkaran yang diputar sejauh 360 ° pada garis tengahnya.")
    
    from PIL import Image
    image = Image.open('PBL1.jpg')
    st.image(image, width=700, caption='Gambar Bola dan Ciri-Cirinya')
    
    st.write("---")
    from PIL import Image
    image = Image.open('PBL2.jpg')
    st.image(image, caption='Rumus Luas Permukaan dan Volume Bola')
    
    st.write("---")
    st.title ('Hitung Luas Permukaan Bola')
     
    st.text ("JIKA DIKETAHUI JARI-JARI BOLA MAKA : ")  
    rb = st.number_input("Masukan jari-jari bola",0)
    HL = st.button ("Hitung luas permukaan dengan jari-jari")
    
    if HL :
        db = 2*rb
        LB = 4*3.14*rb*rb
        st.write ("Diperoleh luas permukaan bola dengan jari-jari di atas adalah", LB )
        st.success(f"kesimpulan : luas permukaan bola dengan jari-jari {rb} cm atau diameter {db} cm adalah {LB} cm2")
        st.balloons()
        
    st.text("JIKA DIKETAHUI DIAMETER MAKA : ")
    db = st.number_input ("masukan ukuran diameter",0)
    HL = st.button ("Hitung luas permukaan")

    if HL :
        rb = 0.5*db
        LB =  4*3.14*rb*rb
        st.write("Diperoleh luas permukaan bola adalah ", LB)
        st.success (f"Kesimpulan : luas permukaan bola dengan diameter {db} cm atau jari-jari {rb} cm adalah {LB} cm2")
        st.snow()
        
