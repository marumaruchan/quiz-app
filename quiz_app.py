import streamlit as st

# クイズの問題と選択肢
question = "Pythonでデータ分析に使うライブラリは？"
options = ["numpy", "pandas", "matplotlib", "全部"]
answer = "全部"

# ユーザーの回答を取得
st.title("データサイエンスクイズ")
st.write(question)
user_answer = st.radio("選択してください", options)

# 回答の判定
if st.button("回答する"):
    if user_answer == answer:
        st.success("正解！🎉")
    else:
        st.error("不正解 😢")