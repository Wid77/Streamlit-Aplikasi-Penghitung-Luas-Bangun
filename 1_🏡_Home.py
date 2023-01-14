import streamlit as st
st.set_page_config(
    page_title="multipage app",
)

st. markdown("<h1 style='text-align: center; color: grey;'>APLIKASI PENGHITUNG LUAS BANGUN DUA DIMENSI DAN TIGA DIMENSI</h1>",  unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: grey;'>👋Selamat Datang Kawan-Kawan👋</h2>", unsafe_allow_html=True)
st.write("---" )
st.markdown("### PENGENALAN APLIKASI")
st.markdown(
    """
    <style>
        img{
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
from PIL import Image
image = Image.open('geo.png')
st.image(image, caption=None)
st.write("Aplikasi penghitung luas bangun ini adalah sebuah aplikasi  atau software yang berbasis website dan dapat diakses melalui browser. Aplikasi ini menawarkan informasi dan fitur dalam membantu menyelesaikan perhitungan matematika khususnya geometri. Geometri merupakan suatu ilmu di dalam sistem matematika yang di dalamnya mempelajari garis, ruang, dan volume yang bersifat abstrak dan berkaitan satu sama lain, mempunyai garis dan titik sehingga menjadi sebuah simbol seperti bentuk persegi, segitiga, lingkaran, dan lain-lain. Aplikasi ini dirancang menggunakan streamlit yang merupakan framework berbasis Python.")
st.write (
        """
        Aplikasi ini mencakup tentang :
        - Informasi berupa penjelasan mengenai jenis-jenis bangun dua dimensi dan tiga dimensi
        - Fitur penghitung luas bangun dua dimensi dan luas permukaan tiga dimensi
        - Informasi tentang pengembang aplikasi 
        """)
st.write("---")

st.markdown("### SEKILAS TENTANG STREAMLIT")
st.video("https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4")
st.markdown("Untuk informasi lebih lanjut, silakan kunjungi [Situs Resmi Streamlit](https://streamlit.io/)")
st.write("---")

st.markdown("<h2 style='text-align: center; color: yellow;'>Selamat Belajar☺</h2>", unsafe_allow_html=True)

st.sidebar.success("Silakan Anda pilih menu di atas")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpapertag.com/wallpaper/middle/8/0/1/350871-website-background-1920x1200-high-resolution.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url(); 







