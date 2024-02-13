import streamlit as st
from PIL import Image
st.set_page_config(page_title="My beloved Baby <3",layout="wide")
#asset
img_menu_f = Image.open("images/my love5.png")

st.title("HAPPY VALENTINE'S DAY BABI!")
st.subheader("This girl is very precious to me, Her name is Marelle Jaylian Real")
st.write("[PRESS THIS MY LOVE](https://www.tiktok.com/@kvrenii/video/6970809933210111237?is_from_webapp=1&sender_device=pc&web_id=7334233675972625922)")

with st.container():
    st.write("---")
    left_c, image_c = st.columns((1,4))
    with left_c:
        st.header("FOR MY BABY")
        st.write("##")
        st.write(
            """
        HI babi, Happy Valentine’s Day! Beside you is my favorite place in the world. I love you so much! Thank you for being always there when i'm sad or at my lowest point
        i made this website for you to show my love for you....
            """
        )
    with image_c:
        st.image(img_menu_f)
        st.write("---")

img_menu_a = Image.open("images/my love4.png")

with st.container():
    image_a, left_a = st.columns((25,12))
    with left_a:
        st.header("MY BABI")
        st.write("##")
        st.write(
            """
            THINGS THAT SHE LIKES

            • she loves playing genshin impact and her fav character is Nahida, Qiqi, Xingqiu
            """
        )
        st.write(
            """
        • she likes eating kare-kare and sweets
            """
        )
        st.write(
            """
        • she wants go to south korea 
            """
        )
        st.write(
            """
        • she loves to send cute videos/pics
            """
        )
        st.write(
            """
        • she likes color pink and purple
            """
        )
    with image_a:
        st.image(img_menu_a)
        st.write("---")

img_menu_b = Image.open("images/my love6.jpg")

with st.container():
    left_b, image_b =st.columns((1,4))
    with left_b:
        st.header("MY LOVE, MY BABI AND MY EVERYTHING")
        st.write("##")
        st.write(
            """ 
            It seems like another day that I first told you that I liked you. it was such a great beginning, and things are now better.
            Living with you is awesome and wonderful.
            Once more, my baby, I love you more than you can possibly know. Happy Valentine's Day, to you, my love 
            """                 
)
    with image_b:
        st.image(img_menu_b)
        st.write("---")
