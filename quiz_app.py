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
        {"question": "Pythonで変数を定義する正しい方法は？", "options": ["var x = 5", "x = 5", "let x = 5"], "answer": "x = 5", "explanation": "Pythonでは変数を宣言する際に型指定は不要です。"},
        {"question": "リストの要素にアクセスする正しい方法は？", "options": ["list[1]", "list.get(1)", "list{1}"], "answer": "list[1]", "explanation": "Pythonではインデックスを角括弧[]で指定します。"},
        {"question": "関数を定義する正しい方法は？", "options": ["def func():", "function func():", "func =>"], "answer": "def func():", "explanation": "Pythonではdefキーワードを使って関数を定義します。"},
        {"question": "条件分岐で正しい記述は？", "options": ["if (x > 5) {}", "if x > 5:", "if x > 5 then"], "answer": "if x > 5:", "explanation": "Pythonでは条件分岐にコロン(:)を使用します。"},
        {"question": "forループの正しい構文は？", "options": ["for (int i=0; i<5; i++)", "for i in range(5):", "foreach i in range(5)"], "answer": "for i in range(5):", "explanation": "Pythonではforループにrange()を使用します。"},
        {"question": "リスト内包表記の正しい使い方は？", "options": ["[x*x for x in range(5)]", "{x*x | x in range(5)}", "(x*x for x in range(5))"], "answer": "[x*x for x in range(5)]", "explanation": "リスト内包表記は角括弧[]を使用します。"},
        {"question": "辞書のキーにアクセスする方法は？", "options": ["dict[\"key\"]", "dict.key", "dict{key}"], "answer": "dict[\"key\"]", "explanation": "辞書のキーは角括弧[]でアクセスします。"},
        {"question": "関数のデフォルト引数を設定する方法は？", "options": ["def func(x=10):", "def func(x: 10):", "func x = 10"], "answer": "def func(x=10):", "explanation": "Pythonではデフォルト引数を=で設定できます。"},
        {"question": "Pythonでコメントを記述する方法は？", "options": ["// コメント", "# コメント", "<!-- コメント -->"], "answer": "# コメント", "explanation": "Pythonでは#を使ってコメントを記述します。"},
        {"question": "タプルとリストの違いは？", "options": ["タプルは変更不可、リストは変更可", "どちらも変更可", "どちらも変更不可"], "answer": "タプルは変更不可、リストは変更可", "explanation": "タプルは変更不可（immutable）ですが、リストは変更可能です。"}
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
    
    
if "current_question" not in st.session_state or "current_stage" not in st.session_state or st.session_state["current_stage"] != stage:
        st.session_state["current_question"] = 0
        st.session_state["answered"] = False
        st.session_state["current_stage"] = stage

question = questions[stage][st.session_state["current_question"]]
    
st.write(f"### {question['question']}")
answer = st.radio("選択肢", question["options"], key="answer_radio")
    
if st.button("回答する"):
        st.session_state["answered"] = True
        if answer == question["answer"]:
            st.success("正解！ 🎉")
        else:
            st.error("不正解 😢")
        st.write("解説: ", question["explanation"])
    
if st.session_state["answered"]:
        if st.button("次の問題", key="next_question"):
            st.session_state["current_question"] = (st.session_state["current_question"] + 1) % len(questions[stage])
            st.session_state["answered"] = False
            st.rerun()  # 画面を更新

if __name__ == "__main__":
    main()
