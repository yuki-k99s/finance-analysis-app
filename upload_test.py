
import streamlit as st

st.title("CSVアップロードテスト")

uploaded_file = st.file_uploader(
    "CSVファイルを選択してください",
    type="csv"
)

if uploaded_file is not None:
    st.success("アップロード成功")
    st.write("ファイル名：", uploaded_file.name)
    st.write("ファイルサイズ：", uploaded_file.size, "バイト")
