import streamlit as st
import random

def main():
    st.title("データサイエンス学習クイズ")

    stage = st.sidebar.selectbox("ステージを選択", [
        "ステージ1: Python基礎", 
        "ステージ2: データ操作", 
        "ステージ3: 可視化", 
        "ステージ4: 統計分析", 
        "ステージ5: 機械学習基礎", 
        "ステージ6: 応用問題チャレンジ！", 
        "ステージ7: 統計解析"])
    
    questions = {
        "ステージ1: Python基礎": [
            {"question": "Pythonでリストを作成する正しい構文は？", "options": ["list = []", "list()", "{}"], "answer": "list = []", "explanation": "Pythonのリストは `list = []` で定義できます。"},
            {"question": "条件分岐に使用するキーワードは？", "options": ["if", "for", "while"], "answer": "if", "explanation": "条件分岐には `if` を使用します。"}
        ],
        "ステージ2: データ操作": [
            {"question": "Pandasでデータの先頭を表示するメソッドは？", "options": ["head()", "tail()", "show()"], "answer": "head()", "explanation": "Pandasの `head()` メソッドはデータフレームの最初の数行を表示します。"},
            {"question": "特定の列を削除するPandasのメソッドは？", "options": ["drop()", "remove()", "delete()"], "answer": "drop()", "explanation": "`drop()` メソッドを使うと、指定した列や行を削除できます。"}
        ],
        "ステージ3: 可視化": [
            {"question": "Matplotlibでヒストグラムを描く関数は？", "options": ["hist()", "plot()", "bar()"], "answer": "hist()", "explanation": "ヒストグラムを描くには `hist()` を使用します。"}
        ],
        "ステージ4: 統計分析": [
            {"question": "データの平均を求める関数は？", "options": ["mean()", "median()", "mode()"], "answer": "mean()", "explanation": "`mean()` は平均値を計算する関数です。"}
        ],
        "ステージ5: 機械学習基礎": [
            {"question": "線形回帰を実装するライブラリは？", "options": ["sklearn", "tensorflow", "numpy"], "answer": "sklearn", "explanation": "`sklearn` を使うと線形回帰モデルを簡単に実装できます。"}
        ],
        "ステージ6: 応用問題チャレンジ！": [
            {"question": "実際のデータを分析する際に重要な前処理は？", "options": ["欠損値処理", "データの削除", "データの無視"], "answer": "欠損値処理", "explanation": "データ分析では欠損値処理が重要なステップです。"}
        ],
        "ステージ7: 統計解析": [
            {"question": "仮説検定でp値が小さい場合の解釈は？", "options": ["帰無仮説を棄却", "帰無仮説を採択", "結果は不明"], "answer": "帰無仮説を棄却", "explanation": "p値が小さい場合、統計的に有意であると判断し、帰無仮説を棄却します。"}
        ]
    }
    
    if stage not in questions:
        st.warning("このステージの問題はまだ追加されていません。")
        return
    
    if "current_question" not in st.session_state:
        st.session_state["current_question"] = 0
    
    if "answered" not in st.session_state:
        st.session_state["answered"] = False
    
    question = questions[stage][st.session_state["current_question"]]
    
    st.write(f"### {question['question']}")
    answer = st.radio("選択肢", question["options"], key=f"answer_radio_{stage}")
    
    if st.button("回答する"):
        st.session_state["answered"] = True
        if answer == question["answer"]:
            st.success("正解！ 🎉")
        else:
            st.error("不正解 😢")
        st.write("解説: ", question["explanation"])
    
    if st.session_state["answered"] and st.button("次の問題"):
        st.session_state["current_question"] = (st.session_state["current_question"] + 1) % len(questions[stage])
        st.session_state["answered"] = False
    
if __name__ == "__main__":
    main()
