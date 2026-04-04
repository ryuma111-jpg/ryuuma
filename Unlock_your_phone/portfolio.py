import streamlit as st
import cv2
import numpy as np
from PIL import Image

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.title("システム解除済み")
    st.success("機密情報へようこそ")
    st.write("書きたくない情報を書きます")

if st.button("ログアウト"):
    st.session_state.logged_in = False
    st.rerun()

else:
    st.title("解除プログラム")

target_img = cv2.imread("Unlock_your_phone/image/peach.jpg")
uploaded_file = st.file_uploader("ドロップしてください",type=["jpg","png","jpeg"])

if target_img is None:
    st.error("画像が読み込めません")
    st.stop()


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    compile_img = np.array(image.convert('RGB'))
    compile_img = cv2.cvtColor(compile_img, cv2.COLOR_RGB2BGR)

    height, width = target_img.shape[:2]
    compile_img = cv2.resize(compile_img, (width,height))
    st.image(compile_img, caption="アップロードされた画像",channels="BGR")
    
    diff = cv2.absdiff(target_img, compile_img)
    result = np.sum(diff)

    if result < 10000:
        st.button("解除")
        st.session_state.logged_in = True
        st.rerun()
    else:
        st.button("ロック")
else:
    st.info("画像をアップロードをしてください")
