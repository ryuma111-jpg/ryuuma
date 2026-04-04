import streamlit as st
import cv2
import numpy as np
import os

image_path = "成果物/image/peach.jpg"

st.title("画像一致判定プログラム")
if result == 0:
        st.success("画像が一致しました！「開く」")
        st.balloons()
else:
        st.error("画像が一致しません。")

