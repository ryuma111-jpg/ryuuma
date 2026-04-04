import streamlit as st
import cv2
import numpy as np
import os


# 「成果物」フォルダの中から見た相対パスにする
target_img = cv2.imread("成果物/image/peach.jpg")
compare_img = cv2.imread("成果物/image/peach.jpg")



st.title("画像一致判定プログラム")
if result == 0:
        st.success("画像が一致しました！「開く」")
        st.balloons()
else:
        st.error("画像が一致しません。")

