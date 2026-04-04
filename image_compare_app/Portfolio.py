import streamlit as st
import cv2
import numpy as np
from PIL import Image



st.title("画像一致判定プログラム!")

target_img = cv2.imread("image/peach.jpg")
if target_img is None:
    st.error("基準画像が読み込めません")
    st.stop()
uploaded_file = st.file_uploader("ドロップしてください",type=["jpg","png","jpeg"])

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
        st.success("正解！！")
        st.balloons()
    else:
       st.write(f"差分スコア: {result}")
else:
    st.info("アップロードをしてください")
