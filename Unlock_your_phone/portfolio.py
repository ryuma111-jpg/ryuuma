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
    image_paths = ["image/peach.jpg", "image/peach1.webp", "image/peach2.jpg"]
    targets = [cv2.imread(p) for p in image_paths]

    if any(t is None for t in targets):
        st.error("画像が読み込めません")
        st.stop()
        
    uploaded_file = st.file_uploader("ドロップしてください",type=["jpg","png","jpeg","webp"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        compile_img = np.array(image.convert('RGB'))
        compile_img = cv2.cvtColor(compile_img, cv2.COLOR_RGB2BGR)

        st.image(compile_img, caption="アップロードされた画像", channels="BGR")

        is_match = False
        best_score = None

        for target_img in targets:
            h, w = target_img.shape[:2]
            temp_img = cv2.resize(compile_img,(w, h))
            diff = cv2.absdiff(target_img, temp_img)

            if np.sum(diff) < 10000:
                is_match = True
                break
        st.write(f"一致度(小さいほど近い):{best_score}")
        if is_match:
            st.success("認証成功")
            if st.button("解除"):
                st.session_state.logged_in = True
                st.rerun()
        else:
            st.error("画像が一致しません")
            st.button("ロック中",disabled = True)
    else:
        st.info("画像をアップロードしてください")