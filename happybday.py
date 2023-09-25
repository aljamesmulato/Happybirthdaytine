import streamlit as st
from PIL import Image
st.set_page_config(page_title="Happy Birthday",layout="wide")
#asset
img_image_1 = Image.open("images/tine.jpg")

st.title("yo, its ya boi alghie😎")
st.write("[click this link <----](https://youtu.be/ykHAwUhjjGE?si=OLG_yUpB0skLrm9P)")

with st.container():
    st.write("---")
    left_1, image_1 = st.columns((1,1))
    with left_1:
        st.header("Happy 17th birthday Tine!")
        st.write("##")
        st.write(
            """
            Happy birthday to you, wish u all the best and more birthdays to come! 
            🎂🎉
            :confetti_ball:
"""
    

        )
    with image_1:
        st.image(img_image_1)
#asset
img_image_2 = Image.open("images/meow.jpg")
    
with st.container():
        st.write("---")
        image_2, left_2 = st.columns((6,1))
with left_2:
     st.header("🐱")
with image_2:
     st.image(img_image_2)