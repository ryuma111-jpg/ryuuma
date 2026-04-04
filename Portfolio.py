import streamlit as st
import cv2
import numpy as np
import os

# GitHub上の構成「成果物/image/peach.jpg」に合わせて指定
image_path = "成果物/image/peach.jpg"

st.title("画像一致判定プログラム")

# ファイルが存在するかチェック
if os.path.exists(image_path):
    target_img = cv2.imread(image_path)
    # 比較用も同じ画像を読み込む（テスト用）
    compare_img = cv2.imread(image_path)

    if target_img is not None:
        height, width = target_img.shape[:2]
        # サイズを合わせる
        compare_img = cv2.resize(compare_img, (width, height))
        # 差分を計算
        diff = cv2.absdiff(target_img, compare_img)
        result = np.sum(diff)
        
        if result == 0:
            st.success("画像が一致しました！「開く」")
            st.balloons()
        else:
            st.error("画像が一致しません。")
    else:
        st.error("画像の読み込みに失敗しました。ファイルが壊れていないか確認してください。")
else:
    # どこを探しているか画面に表示して確認しやすくする
    st.error(f"画像ファイルが見つかりません。現在のパス設定: {image_path}")
    st.info("GitHub上で『成果物』フォルダの中に『image』フォルダがあるか確認してください。")
