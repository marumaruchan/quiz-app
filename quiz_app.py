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
        "ステージ7: 統計解析"
    ])
    
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
            {"question": "6.散布図を描くためのMatplotlibの関数は？", "options": ["scatter()", "plot()", "points()"], "answer": "scatter()", "explanation": "`scatter()` 関数を使用して散布図を描きます。"},
            {"question": "7.データのトレンドを描く関数は？", "options": ["plot()", "trend()", "line()"], "answer": "plot()", "explanation": "`plot()` 関数でデータのトレンドを描画できます。"},
            {"question": "8.多重プロットを行うためのSeabornのメソッドは？", "options": ["facetgrid()", "subplot()", "multiplot()"], "answer": "facetgrid()", "explanation": "`facetgrid()` を使うことで多重プロットを作成できます。"},
            {"question": "9.ヒートマップを描くための関数は？", "options": ["heatmap()", "map()", "color_map()"], "answer": "heatmap()", "explanation": "`heatmap()` 関数を使ってデータのヒートマップを可視化します。"},
            {"question": "10.MatplotlibでX軸とY軸にラベルを設定するメソッドは？", "options": ["set_xlabel(), set_ylabel()", "xlabel(), ylabel()", "label_x(), label_y()"], "answer": "set_xlabel(), set_ylabel()", "explanation": "X軸とY軸のラベルはそれぞれ `set_xlabel()` と `set_ylabel()` で設定します。"}
        ],
        "ステージ4: 統計分析": [
            {"question": "1.標準偏差を計算する関数は？", "options": ["std()", "stdev()", "variance()"], "answer": "std()", "explanation": "標準偏差は `std()` で計算されます。"},
            {"question": "2.平均を計算する関数は？", "options": ["avg()", "mean()", "average()"], "answer": "mean()", "explanation": "平均は `mean()` で計算されます。"},
            {"question": "3.相関係数を計算するメソッドは？", "options": ["corr()", "correlation()", "cov()"], "answer": "corr()", "explanation": "相関係数は `corr()` で計算できます。"},
            {"question": "4.回帰分析のためのライブラリは？", "options": ["Scikit-learn", "Numpy", "Pandas"], "answer": "Scikit-learn", "explanation": "回帰分析にはScikit-learnがよく使用されます。"},
            {"question": "5.確率分布を描くための関数は？", "options": ["probability()", "dist()", "pdf()"], "answer": "pdf()", "explanation": "確率分布関数は `pdf()` で描画されます。"},
            {"question": "6.中央値を計算するメソッドは？", "options": ["median()", "middle()", "avg()"], "answer": "median()", "explanation": "中央値は `median()` メソッドで計算されます。"},
            {"question": "7.四分位範囲を求めるメソッドは？", "options": ["iqr()", "quantile()", "range()"], "answer": "quantile()", "explanation": "四分位範囲は `quantile()` メソッドを使って求めます。"},
            {"question": "8.ヒストグラムを描く関数は？", "options": ["hist()", "frequency()", "plot()"], "answer": "hist()", "explanation": "ヒストグラムは `hist()` で描画されます。"},
            {"question": "9.信頼区間を計算するための方法は？", "options": ["confidence_interval()", "ci()", "calc_ci()"], "answer": "confidence_interval()", "explanation": "信頼区間は `confidence_interval()` メソッドで計算されます。"},
            {"question": "10.異常値を検出する方法は？", "options": ["outlier_detection()", "find_outliers()", "z_score()"], "answer": "z_score()", "explanation": "Zスコアを使って異常値を検出します。"}
        ],
        "ステージ5: 機械学習基礎": [
            {"question": "1.教師あり学習とは何か？", "options": ["ラベル付きデータを使用する", "ラベルなしデータを使用する", "データをクラスタリングする"], "answer": "ラベル付きデータを使用する", "explanation": "教師あり学習はラベル付きデータでモデルを学習させます。"},
            {"question": "2.データの前処理で行うべきことは？", "options": ["欠損値の処理", "正規化", "すべての選択肢"], "answer": "すべての選択肢", "explanation": "前処理には欠損値の処理や正規化が含まれます。"},
            {"question": "3.過学習とは何か？", "options": ["モデルが訓練データに適合しすぎる", "モデルがデータを学習しない", "モデルがデータを適切に学習する"], "answer": "モデルが訓練データに適合しすぎる", "explanation": "過学習はモデルが訓練データに過剰に適合している状態です。"},
            {"question": "4.特徴量エンジニアリングとは何か？", "options": ["データを正規化する", "新しい特徴量を作成する", "モデルを選択する"], "answer": "新しい特徴量を作成する", "explanation": "特徴量エンジニアリングは新しい特徴量を作成するプロセスです。"},
            {"question": "5.モデル評価指標としてよく使用されるものは？", "options": ["精度", "再現率", "すべての選択肢"], "answer": "すべての選択肢", "explanation": "精度や再現率などがモデル評価に使用されます。"},
            {"question": "6.線形回帰の目的は？", "options": ["予測", "分類", "クラスタリング"], "answer": "予測", "explanation": "線形回帰は数値予測のための手法です。"},
            {"question": "7.サポートベクターマシン(SVM)の目的は？", "options": ["データを分類する", "データをクラスタリングする", "予測する"], "answer": "データを分類する", "explanation": "SVMは分類問題に使われる手法です。"},
            {"question": "8.決定木の特徴は？", "options": ["ツリー構造で可視化できる", "数値データのみ使用", "線形関係のみ考慮"], "answer": "ツリー構造で可視化できる", "explanation": "決定木はツリー構造で視覚的に表現できます。"},
            {"question": "9.ニューラルネットワークの基本的な単位は？", "options": ["ノード", "ユニット", "パラメータ"], "answer": "ノード", "explanation": "ニューラルネットワークの基本的な単位はノードです。"},
            {"question": "10.交差検証の目的は？", "options": ["モデルの汎化能力を評価する", "データを可視化する", "訓練データを生成する"], "answer": "モデルの汎化能力を評価する", "explanation": "交差検証はモデルの汎化能力を測るために使います。"}
        ],
        "ステージ6: 応用問題チャレンジ！": [
            {"question": "1.データサイエンスプロジェクトの最初のステップは？", "options": ["データの取得", "モデルの選定", "結果の評価"], "answer": "データの取得", "explanation": "プロジェクトはデータの取得から始まります。"},
            {"question": "2.データの可視化に役立つライブラリは？", "options": ["Numpy", "Matplotlib", "Requests"], "answer": "Matplotlib", "explanation": "データの可視化にはMatplotlibがよく使われます。"},
            {"question": "3.データクリーニングの目的は？", "options": ["データを整理する", "無駄な情報を削除する", "分析しやすくする"], "answer": "すべての選択肢", "explanation": "データクリーニングはデータを整理し、無駄な情報を削除します。"},
            {"question": "4.バイアスとバリアンスのトレードオフを理解することが重要な理由は？", "options": ["モデルのパフォーマンスを向上させるため", "データの可視化に役立つため", "アルゴリズムを選ぶため"], "answer": "モデルのパフォーマンスを向上させるため", "explanation": "バイアスとバリアンスのトレードオフはモデルの精度に直接影響します。"},
            {"question": "5.モデルを改善するために行うべきことは？", "options": ["データの増加", "特徴量の選択", "すべての選択肢"], "answer": "すべての選択肢", "explanation": "モデル改善のためには様々な手法を用いることが重要です。"},
            {"question": "6.次元削減の技術としてよく使用されるものは？", "options": ["PCA", "t-SNE", "すべての選択肢"], "answer": "すべての選択肢", "explanation": "PCAやt-SNEなど、次元削減技術はいくつか存在します。"},
            {"question": "7.モデルの性能を評価するための手法は？", "options": ["混同行列", "ROC曲線", "すべての選択肢"], "answer": "すべての選択肢", "explanation": "混同行列やROC曲線などの手法でモデルの性能を評価します。"},
            {"question": "8.アンサンブル学習の目的は？", "options": ["複数のモデルを組み合わせる", "単一のモデルを改善する", "データを整理する"], "answer": "複数のモデルを組み合わせる", "explanation": "アンサンブル学習は複数のモデルの組み合わせによって精度を向上させる手法です。"},
            {"question": "9.データのバイアスを確認するために行うべきことは？", "options": ["データ分布の可視化", "データクリーニング", "特徴量エンジニアリング"], "answer": "データ分布の可視化", "explanation": "データのバイアスを確認するためにはデータ分布を可視化することが重要です。"},
            {"question": "10.強化学習の基本的な要素は？", "options": ["エージェント", "環境", "報酬", "すべての選択肢"], "answer": "すべての選択肢", "explanation": "強化学習ではエージェント、環境、報酬の3つの要素が基本です。"}
        ],
        "ステージ7: 統計解析": [
            {"question": "1.仮説検定の目的は？", "options": ["母集団の特性を推定する", "データの分布を分析する", "ある仮説が正しいかどうかを判断する"], "answer": "ある仮説が正しいかどうかを判断する", "explanation": "仮説検定は仮説の正当性を検証するために行います。"},
            {"question": "2.確率分布の一つである正規分布の特徴は？", "options": ["平均が中央値と等しい", "左右対称", "すべての選択肢"], "answer": "すべての選択肢", "explanation": "正規分布は平均と中央値が等しく、左右対称です。"},
            {"question": "3.相関係数の値の範囲は？", "options": ["0から1", "-1から1", "-∞から∞"], "answer": "-1から1", "explanation": "相関係数は-1から1の範囲を持ちます。"},
            {"question": "4.母集団の平均を推定するために使う推定値は？", "options": ["標本平均", "標本中央値", "標本分散"], "answer": "標本平均", "explanation": "母集団の平均を推定するには標本平均を使用します。"},
            {"question": "5.分散分析(ANOVA)の目的は？", "options": ["複数の群の平均を比較する", "データの散らばりを分析する", "相関関係を調べる"], "answer": "複数の群の平均を比較する", "explanation": "分散分析は異なる群の平均を比較するために用います。"},
            {"question": "6.帰無仮説とは何か？", "options": ["特に差がないという仮説", "特に差があるという仮説", "データの正確性に関する仮説"], "answer": "特に差がないという仮説", "explanation": "帰無仮説は特に差がないことを前提とした仮説です。"},
            {"question": "7.有意水準とは何か？", "options": ["仮説検定での誤差率", "データの分布の範囲", "データの中央値"], "answer": "仮説検定での誤差率", "explanation": "有意水準は誤判定の許容される確率です。"},
            {"question": "8.統計的仮説検定の手法の一つは？", "options": ["t検定", "Z検定", "すべての選択肢"], "answer": "すべての選択肢", "explanation": "t検定やZ検定など、様々な手法があります。"},
            {"question": "9.標準正規分布とは何か？", "options": ["平均0、分散1の正規分布", "平均1、分散0の正規分布", "平均0、分散0の正規分布"], "answer": "平均0、分散1の正規分布", "explanation": "標準正規分布は平均0、分散1の正規分布です。"},
            {"question": "10.確率変数とは何か？", "options": ["数値が変化する変数", "確率を持つ変数", "特定の値を持つ変数"], "answer": "確率を持つ変数", "explanation": "確率変数は確率を持つ変数です。"}
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