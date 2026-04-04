import streamlit as st
import cv2
import numpy as np
import os

image_path = "成果物/image/peach.jpg"

st.title("画像一致判定プログラム")

# ファイルが存在するかチェック

        
        if result == 0:
            st.success("画像が一致しました！「開く」")
            st.balloons()
        else:
            st.error("画像が一致しません。")
    else:
        st.error("画像の読み込みに失敗しました（データ形式を確認してください）")
else:
    st.error(f"画像ファイルが見つかりません。パスを確認してください: {image_path}")

