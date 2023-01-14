import streamlit as st
st.set_page_config(
    page_title="multipage app",
)

st. markdown("<h1 style='text-align: center; color: orange;'>PROFILE DEVELOPER</h1>",  unsafe_allow_html=True)
st.write("---")

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
image = Image.open('wid.jpg')
st.image(image, caption=None)

st.write (
        """
        - Nama : I GEDE WIDNYANA
        - Umur : 19 tahun
        - Jenis kelamin : Laki-laki
        - Universitas : Universitas Udayana
        - Program Studi : S1-Informatika
        - Media sosial : [Instagram](https://instagram.com/gede.widd?igshid=YmMyMTA2M2Y=) | [Email](mailto:peoplesimple6@gmail.com)
        """)

st.write("---")

st.markdown("<h2 style='text-align: center; color: yellow;'>Salam Kenal🙌</h2>", unsafe_allow_html=True)
st.balloons()

st.image('PA.jpg', width=700, caption="Teman-Teman Seperjuangan", use_column_width=False, clamp=True, channels='RGB')

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2015/05/07/22/00/blue-757265_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url(); 



