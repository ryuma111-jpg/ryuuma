import streamlit as st
import cv2
import numpy as np

target_img = cv2.imread("image/peach.jpg")
compare_img = cv2.imread("image/peach.jpg")
if target_img is not None and compare_img is not None:
    height, width = target_img.shape[:2]
    compare_img = cv2.resize(compare_img, (width, height))
    diff = cv2.absdiff(target_img, compare_img)
    result = np.sum(diff)
   
if result == 0:
    st.success("開く")
    st.balloons()
else:
    st.error("開かない")
