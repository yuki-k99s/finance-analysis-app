import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
from matplotlib import font_manager

# 日本語フォントを設定
font_manager.fontManager.addfont(
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc")

plt.rcParams["font.family"] = "Noto Sans CJK JP"

# 最高利益・最低利益・平均利益・カウント抽出関数
def analyze_profit(months, profits):
    # 最高利益
    max_profit = max(profits)
    max_index = profits.index(max_profit)
    max_month = months[max_index]
    # 最低利益
    min_profit = min(profits)
    min_index = profits.index(min_profit)
    min_month = months[min_index]
    # 平均利益
    average_profit = sum(profits) / len(profits)
    # カウンター
    plus_count = 0
    minus_count = 0
    zero_count = 0
    for profit in profits:
        if profit > 0:
            plus_count += 1

        elif profit < 0:
            minus_count += 1

        else:
            zero_count += 1
    # 値を返す
    return max_month, max_profit, min_month, min_profit, average_profit, plus_count, minus_count, zero_count

st.title("収支分析アプリ")

uploaded_file = st.file_uploader("CSVファイルを選択してください", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # 利益を計算
    df["profit"] = df["income"] - df["expense"]

    # リストに変換
    months = df["month"].tolist()
    profits = df["profit"].tolist()
    
    # データを表示
    st.write("読み込んだデータ")
    st.dataframe(df)

    # 確認用
    st.write("月のリスト：", months)
    st.write("利益のリスト：", profits)

    max_month, max_profit, min_month, min_profit, average_profit, plus_count, minus_count, zero_count = analyze_profit(months, profits)

    st.write("最高利益：", max_month, max_profit, "円")
    st.write("最低利益：", min_month, min_profit, "円")
    st.write("平均利益：", average_profit, "円")
    st.write("黒字月数：", plus_count, "回")
    st.write("赤字月数：", minus_count, "回")
    st.write("収支均衡月数：", zero_count, "回")

    # 月別利益グラフ
    fig, ax = plt.subplots()

    ax.bar(months, profits)
    ax.axhline(0, color="gray")

    ax.set_title("月別利益")
    ax.set_xlabel("月")
    ax.set_ylabel("利益（円）")
    
    st.pyplot(fig)
    plt.close(fig)
