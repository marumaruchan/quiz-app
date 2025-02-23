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
        {"question": "1.Pythonで変数を定義する正しい方法は？", "options": ["var x = 5", "x = 5", "let x = 5"], "answer": "x = 5", "explanation": "Pythonでは変数を宣言する際に型指定は不要です。"},
        {"question": "2.リストの要素にアクセスする正しい方法は？", "options": ["list[1]", "list.get(1)", "list{1}"], "answer": "list[1]", "explanation": "Pythonではインデックスを角括弧[]で指定します。"},
        {"question": "3.関数を定義する正しい方法は？", "options": ["def func():", "function func():", "func =>"], "answer": "def func():", "explanation": "Pythonではdefキーワードを使って関数を定義します。"},
        {"question": "4.条件分岐で正しい記述は？", "options": ["if (x > 5) {}", "if x > 5:", "if x > 5 then"], "answer": "if x > 5:", "explanation": "Pythonでは条件分岐にコロン(:)を使用します。"},
        {"question": "5.forループの正しい構文は？", "options": ["for (int i=0; i<5; i++)", "for i in range(5):", "foreach i in range(5)"], "answer": "for i in range(5):", "explanation": "Pythonではforループにrange()を使用します。"},
        {"question": "6.リスト内包表記の正しい使い方は？", "options": ["[x*x for x in range(5)]", "{x*x | x in range(5)}", "(x*x for x in range(5))"], "answer": "[x*x for x in range(5)]", "explanation": "リスト内包表記は角括弧[]を使用します。"},
        {"question": "7.辞書のキーにアクセスする方法は？", "options": ["dict[\"key\"]", "dict.key", "dict{key}"], "answer": "dict[\"key\"]", "explanation": "辞書のキーは角括弧[]でアクセスします。"},
        {"question": "8.関数のデフォルト引数を設定する方法は？", "options": ["def func(x=10):", "def func(x: 10):", "func x = 10"], "answer": "def func(x=10):", "explanation": "Pythonではデフォルト引数を=で設定できます。"},
        {"question": "9.Pythonでコメントを記述する方法は？", "options": ["// コメント", "# コメント", "<!-- コメント -->"], "answer": "# コメント", "explanation": "Pythonでは#を使ってコメントを記述します。"},
        {"question": "10.タプルとリストの違いは？", "options": ["タプルは変更不可、リストは変更可", "どちらも変更可", "どちらも変更不可"], "answer": "タプルは変更不可、リストは変更可", "explanation": "タプルは変更不可（immutable）ですが、リストは変更可能です。"}
    ],
    "ステージ2: データ操作": [
        {"question": "1.Pandasでデータフレームの最初の5行を表示するメソッドは？", "options": ["show()", "head()", "display()"], "answer": "head()", "explanation": "`head()` メソッドを使うと最初の5行が表示されます。"},
        {"question": "2.データフレームの列を取得する方法は？", "options": ["df['列名']", "df.column(列名)", "df->列名"], "answer": "df['列名']", "explanation": "列を取得するには `df['列名']` を使います。"},
        {"question": "3.欠損値を削除するメソッドは？", "options": ["dropna()", "fillna()", "replace()"], "answer": "dropna()", "explanation": "欠損値を削除するには `dropna()` を使います。"},
        {"question": "4.データフレームの行数を取得するには？", "options": ["len(df)", "df.shape[0]", "df.rows"], "answer": "df.shape[0]", "explanation": "行数を取得するには `df.shape[0]` を使います。"},
        {"question": "5.列の平均値を計算するには？", "options": ["df.mean()", "df.average()", "df.sum()/df.count()"], "answer": "df.mean()", "explanation": "`mean()` を使うと平均値を計算できます。"},
        {"question": "6.データフレームのソートに使うメソッドは？", "options": ["sort_values()", "order_by()", "sort()"], "answer": "sort_values()", "explanation": "データフレームをソートするには `sort_values()` を使います。"},
        {"question": "7.データフレームを結合するメソッドは？", "options": ["merge()", "concat()", "combine()"], "answer": "merge()", "explanation": "データを結合するには `merge()` を使います。"},
        {"question": "8.データフレームの行をフィルタリングする方法は？", "options": ["df[df['列名'] > 10]", "df.filter('列名' > 10)", "df.where('列名' > 10)"], "answer": "df[df['列名'] > 10]", "explanation": "条件を指定してフィルタリングできます。"},
        {"question": "9.データフレームをCSVファイルとして保存するには？", "options": ["df.to_csv()", "df.save_csv()", "df.write_csv()"], "answer": "df.to_csv()", "explanation": "`to_csv()` メソッドでCSVとして保存できます。"},
        {"question": "10.データフレームのインデックスをリセットするメソッドは？", "options": ["reset_index()", "set_index()", "drop_index()"], "answer": "reset_index()", "explanation": "`reset_index()` を使うとインデックスをリセットできます。"}
    ],
        "ステージ3: 可視化": [
        {"question": "1.Matplotlibでヒストグラムを描く関数は？", "options": ["hist()", "plot()", "bar()"], "answer": "hist()", "explanation": "`hist()` を使うとヒストグラムを描画できます。"},
        {"question": "2.Seabornでペアプロットを描画する関数は？", "options": ["pairplot()", "scatter()", "heatmap()"], "answer": "pairplot()", "explanation": "`pairplot()` は変数間の関係を視覚化するために使います。"},
        {"question": "3.Matplotlibでタイトルを設定するメソッドは？", "options": ["set_title()", "title()", "plot_title()"], "answer": "title()", "explanation": "`title()` メソッドを使用してグラフにタイトルを設定できます。"},
        {"question": "4.Pandasのデータフレームを棒グラフで可視化するメソッドは？", "options": ["bar()", "plot.bar()", "barplot()"], "answer": "plot.bar()", "explanation": "PandasのDataFrameオブジェクトでは `plot.bar()` を使用して棒グラフを作成できます。"},
        {"question": "5.Seabornでカテゴリ別に箱ひげ図を描画する関数は？", "options": ["boxplot()", "barplot()", "violinplot()"], "answer": "boxplot()", "explanation": "`boxplot()` を使うとカテゴリごとのデータ分布を可視化できます。"},
        {"question": "6.Matplotlibで軸ラベルを設定するには？", "options": ["xlabel() / ylabel()", "set_axis_label()", "axis_label()"], "answer": "xlabel() / ylabel()", "explanation": "Matplotlibでは `xlabel()` と `ylabel()` を使って軸ラベルを設定します。"},
        {"question": "7.Matplotlibで凡例を表示するメソッドは？", "options": ["legend()", "show_legend()", "display_legend()"], "answer": "legend()", "explanation": "`legend()` メソッドを使うと凡例を表示できます。"},
        {"question": "8.散布図を描画するMatplotlib関数は？", "options": ["scatter()", "dotplot()", "points()"], "answer": "scatter()", "explanation": "`scatter()` を使うと散布図を描くことができます。"},
        {"question": "9.ヒートマップを作成するSeaborn関数は？", "options": ["heatmap()", "colorplot()", "matrixplot()"], "answer": "heatmap()", "explanation": "`heatmap()` を使うと行列データのヒートマップを描くことができます。"},
        {"question": "10.Matplotlibで折れ線グラフを描く関数は？", "options": ["plot()", "lineplot()", "curve()"], "answer": "plot()", "explanation": "`plot()` 関数を使うと折れ線グラフを描くことができます。"}
    ],
        "ステージ4: 統計分析": [
        {"question": "1.データの中央値を求める関数は？", "options": ["mean()", "median()", "mode()"], "answer": "median()", "explanation": "中央値を求めるには `median()` を使います。"},
        {"question": "2.標準偏差を求める関数は？", "options": ["std()", "var()", "mean()"], "answer": "std()", "explanation": "`std()` は標準偏差を計算する関数です。"},
        {"question": "3.データの分散を求める関数は？", "options": ["variance()", "std()", "var()"], "answer": "var()", "explanation": "`var()` はデータの分散を求める関数です。"},
        {"question": "4.相関係数を求める関数は？", "options": ["corr()", "cov()", "correlation()"], "answer": "corr()", "explanation": "`corr()` は相関係数を求める関数です。"},
        {"question": "5.正規分布に従うデータを生成する関数は？", "options": ["randn()", "random()", "normal()"], "answer": "normal()", "explanation": "`normal()` は正規分布に従うデータを生成します。"},
        {"question": "6.仮説検定で帰無仮説を棄却する基準となる値は？", "options": ["p値", "t値", "z値"], "answer": "p値", "explanation": "p値が一定の閾値より小さい場合、帰無仮説を棄却します。"},
        {"question": "7.母集団の平均を推定するために使用する統計量は？", "options": ["標本平均", "母平均", "標本分散"], "answer": "標本平均", "explanation": "標本平均は母集団の平均を推定するために使用されます。"},
        {"question": "8.二つのデータセットの関係を示す指標は？", "options": ["相関係数", "標準偏差", "中央値"], "answer": "相関係数", "explanation": "相関係数は二つのデータセットの関連性を示します。"},
        {"question": "9.統計的に有意な結果を示すために一般的に使用されるp値の閾値は？", "options": ["0.05", "0.5", "0.01"], "answer": "0.05", "explanation": "p値が0.05未満の場合、統計的に有意とされることが多いです。"},
        {"question": "10.t検定とは何を比較するための手法？", "options": ["2つの平均", "データの分布", "カテゴリの関連性"], "answer": "2つの平均", "explanation": "t検定は2つのグループの平均値が統計的に異なるかを確認するための手法です。"}
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
