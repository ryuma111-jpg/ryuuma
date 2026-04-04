import streamlit as st
import cv2
import numpy as np
from PIL import Image



st.title("画像一致判定プログラム")

target_img = cv2.imread("image/peach.jpg")
uploaded_file = st.file_uploader("ドロップしてください",type=["jpg","png","jpeg"])
# ファイルが存在するかチェック
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    compile_img = np.array(image.convert('RGB'))
    compile_img = cv2.cvtColor(compile_img, cv2.COLOR_RGB2BGR)
    height, widht = target_img.shape[:2]
    compile_img = cv2.resize(compile_img, (widht,height))
    st.image(compile_img, caption="アップロードされた画像",channels="BGR")
    diff = cv2.absdiff(target_img, compile_img)
    result = np.sum(diff)
    if result < 10000:
        st.success("正解！！")
        st.balloons()
    else:
        st.error("残念")
else:
    st.info("アップロードをしてください")