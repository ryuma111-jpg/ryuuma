import streamlit as st
import cv2
import numpy as np
import os

image_path = "image/peach.jpg"

st.title("画像一致判定プログラム")

if os.path.exists(image_path):
    target_img = cv2.imread(image_path)
    compare_img = cv2.imread(image_path)

    if target_img is not None:
        height, width = target_img.shape[:2]
        compare_img = cv2.resize(compare_img, (width, height))
        diff = cv2.absdiff(target_img, compare_img)
        result = np.sum(diff)
        
        if result == 0:
            st.success("画像が一致しました！「開く」")
            st.balloons()
        else:
            st.error("画像が一致しません。")
