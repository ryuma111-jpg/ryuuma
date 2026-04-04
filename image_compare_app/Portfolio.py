import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("画像一致判定プログラム!")

target_img = cv2.imread("image/peach.jpg")

st.write("ここ通ってる？")  # デバッグ

if target_img is None:
    st.error("基準画像が読み込めません")
    st.stop()
