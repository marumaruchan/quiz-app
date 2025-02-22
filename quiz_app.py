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
        {"question": "Matplotlibでヒストグラムを作成する関数は？", "options": ["hist()", "scatter()", "boxplot()"], "answer": "hist()", "explanation": "Matplotlibの `hist()` を使うとデータの分布を確認できます。"},
        {"question": "Seabornで散布図を描画する関数は？", "options": ["scatterplot()", "lineplot()", "barplot()"], "answer": "scatterplot()", "explanation": "Seabornの `scatterplot()` は散布図を作成するために使用されます。"}
    ],
    "ステージ4: 統計分析": [
        {"question": "データの平均を求めるメソッドは？", "options": ["mean()", "median()", "std()"], "answer": "mean()", "explanation": "`mean()` はデータの平均値を求める関数です。"},
        {"question": "相関係数を求めるPandasのメソッドは？", "options": ["corr()", "cov()", "describe()"], "answer": "corr()", "explanation": "`corr()` は変数間の相関係数を計算します。"}
    ],
    "ステージ5: 機械学習基礎": [
        {"question": "線形回帰を行うためのScikit-learnのクラスは？", "options": ["LinearRegression", "LogisticRegression", "DecisionTree"], "answer": "LinearRegression", "explanation": "`LinearRegression` は線形回帰モデルを作成するためのクラスです。"},
        {"question": "ロジスティック回帰に使用する関数は？", "options": ["LogisticRegression", "SVM", "KMeans"], "answer": "LogisticRegression", "explanation": "`LogisticRegression` は分類問題に適した回帰モデルです。"}
    ],
    "ステージ6: 応用問題チャレンジ！": [
        {"question": "時系列データのトレンド分析に適した手法は？", "options": ["移動平均", "クラスター分析", "PCA"], "answer": "移動平均", "explanation": "移動平均を使うと時系列データのトレンドを滑らかに表示できます。"},
        {"question": "データの異常検知に使われる手法は？", "options": ["Isolation Forest", "線形回帰", "k近傍法"], "answer": "Isolation Forest", "explanation": "`Isolation Forest` は異常検知のためのアルゴリズムです。"}
    ],
    "ステージ7: 統計解析": [
        {"question": "p値の意味は？", "options": ["有意性の指標", "データの平均", "標準偏差"], "answer": "有意性の指標", "explanation": "p値は仮説検定で結果の有意性を示す指標です。"},
        {"question": "単回帰分析で目的変数と説明変数の関係を表す式は？", "options": ["y = ax + b", "y = ax^2 + bx + c", "y = a/b"], "answer": "y = ax + b", "explanation": "単回帰分析では `y = ax + b` の形の線形関係を求めます。"}
    ]
}

 # セッションに現在の問題を保存する
if "current_question" not in st.session_state or st.session_state.stage != stage:
        st.session_state.stage = stage  # ステージを変更した場合、新しい問題を取得
        st.session_state.current_question = random.choice(questions[stage])
        st.session_state.answered = False  # 回答フラグをリセット
    
    question = st.session_state.current_question
    st.subheader(question["question"])
    
    answer = st.radio("選択肢", question["options"], key="answer_radio")
    
    # 回答ボタン
if st.button("回答する"):
        if answer == question["answer"]:
            st.success("正解！")
        else:
            st.error(f"不正解。正解は {question['answer']} です。")
        st.info(question["explanation"])
        st.session_state.answered = True  # 回答済みにする
    
    # 「次の問題」ボタン（回答後のみ表示）
if st.session_state.answered and st.button("次の問題"):
        st.session_state.current_question = random.choice(questions[stage])  # 新しい問題をセット
        st.session_state.answered = False  # 回答フラグをリセット
        st.experimental_rerun()  # ページをリロード

if __name__ == "__main__":
    main()