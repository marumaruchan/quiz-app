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
        "ステージ5: 機械学習基礎":[
        {"question": "1.線形回帰モデルを提供するライブラリは？", "options": ["sklearn", "matplotlib", "numpy"], "answer": "sklearn", "explanation": "`scikit-learn` (sklearn) は機械学習用のライブラリです。"},
        {"question": "2.教師あり学習に含まれる手法は？", "options": ["回帰", "クラスタリング", "次元削減"], "answer": "回帰", "explanation": "教師あり学習には回帰や分類があります。"},
        {"question": "3.分類問題に使われる手法は？", "options": ["ロジスティック回帰", "k-means", "主成分分析"], "answer": "ロジスティック回帰", "explanation": "ロジスティック回帰は分類問題に用いられます。"},
        {"question": "4.k近傍法（k-NN）はどのような手法？", "options": ["教師なし学習", "教師あり学習", "強化学習"], "answer": "教師あり学習", "explanation": "k-NNは教師あり学習の手法の一つです。"},
        {"question": "5.ニューラルネットワークの基本的な単位は？", "options": ["ニューロン", "ノード", "エッジ"], "answer": "ニューロン", "explanation": "ニューラルネットワークは複数のニューロンで構成されています。"},
        {"question": "6.サポートベクターマシン（SVM）の主な目的は？", "options": ["回帰分析", "データ分類", "特徴抽出"], "answer": "データ分類", "explanation": "SVMはデータを分類するための手法です。"},
        {"question": "7.ディープラーニングのフレームワークは？", "options": ["TensorFlow", "Matplotlib", "Pandas"], "answer": "TensorFlow", "explanation": "TensorFlowはディープラーニング向けのフレームワークです。"},
        {"question": "8.決定木の分岐条件を決める要素は？", "options": ["エントロピー", "重み", "学習率"], "answer": "エントロピー", "explanation": "エントロピーは決定木の分岐条件を決める指標です。"},
        {"question": "9.機械学習モデルの過学習を防ぐ方法は？", "options": ["正則化", "データ拡張", "特徴抽出"], "answer": "正則化", "explanation": "正則化は過学習を防ぐための手法の一つです。"},
        {"question": "10.勾配降下法の目的は？", "options": ["損失関数の最小化", "データの可視化", "特徴の選択"], "answer": "損失関数の最小化", "explanation": "勾配降下法は損失関数を最小化するための最適化手法です。"}
    ],
{
  "ステージ6: 応用問題チャレンジ": [
    {
      "question": "1.次元削減に使用される手法は？",
      "options": ["PCA", "回帰分析", "ロジスティック回帰"],
      "answer": "PCA",
      "explanation": "PCA（主成分分析）は次元削減のための手法です。"
    },
    {
      "question": "2.欠損値処理の一般的な方法は？",
      "options": ["削除", "平均値で補完", "どちらも可能"],
      "answer": "どちらも可能",
      "explanation": "dropna() で削除、fillna() で補完ができます。"
    },
    {
      "question": "3.精度の高いモデルを作るために必要なことは？",
      "options": ["特徴量エンジニアリング", "データの削減", "計算機の性能向上"],
      "answer": "特徴量エンジニアリング",
      "explanation": "適切な特徴量を作ることでモデルの精度が向上します。"
    },
    {
      "question": "4.Pythonでニューラルネットワークを作成するライブラリは？",
      "options": ["TensorFlow", "Matplotlib", "Pandas"],
      "answer": "TensorFlow",
      "explanation": "TensorFlow はディープラーニング用のライブラリです。"
    },
    {
      "question": "5.異常検知に使われる手法は？",
      "options": ["k近傍法", "ロジスティック回帰", "サポートベクターマシン"],
      "answer": "サポートベクターマシン",
      "explanation": "SVM は異常検知にも利用されます。"
    },
    {
      "question": "6.モデルの過学習を検出する方法は？",
      "options": ["訓練データの精度のみを見る", "テストデータの精度と比較する", "エポック数を増やす"],
      "answer": "テストデータの精度と比較する",
      "explanation": "訓練データとテストデータの精度差が大きいと過学習の可能性があります。"
    },
    {
      "question": "7.強化学習で報酬を最大化するための手法は？",
      "options": ["Q学習", "回帰分析", "クラスタリング"],
      "answer": "Q学習",
      "explanation": "Q学習 は強化学習の代表的なアルゴリズムです。"
    },
    {
      "question": "8.ベイズ統計が用いられる場面は？",
      "options": ["スパムメール分類", "物理シミュレーション", "データのソート"],
      "answer": "スパムメール分類",
      "explanation": "ナイーブベイズ はスパムフィルタなどで使われます。"
    },
    {
      "question": "9.ハイパーパラメータのチューニング方法は？",
      "options": ["グリッドサーチ", "ランダムサーチ", "どちらも正しい"],
      "answer": "どちらも正しい",
      "explanation": "GridSearchCV や RandomizedSearchCV を使用して調整します。"
    },
    {
      "question": "10.予測モデルの評価をする際に使われるデータは？",
      "options": ["テストデータ", "訓練データ", "ラベルなしデータ"],
      "answer": "テストデータ",
      "explanation": "テストデータは未知のデータに対するモデルの評価に使います。"
    }
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
