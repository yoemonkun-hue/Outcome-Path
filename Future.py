import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("🚀 Future Outcomes Simulator")

# 入力セクション
st.sidebar.header("現在の設定")
effort = st.sidebar.slider("今日の努力量 (0-100)", 0, 100, 50)
years = st.sidebar.slider("期間 (年)", 1, 10, 5)

# 計算ロジック (複利計算を模したモデル)
# 成果 = (努力量 / 50)^2 * 時間
days = np.linspace(0, years, 100)
outcome_curve = (effort / 50)**2 * (days ** 1.5)

# グラフ作成
fig, ax = plt.subplots()
ax.plot(days, outcome_curve, label="Your Growth Path", color="#1f77b4", linewidth=2)
ax.set_xlabel("Years")
ax.set_ylabel("Accumulated Outcomes")
ax.set_title("Future Growth Projection")
ax.grid(True, linestyle='--', alpha=0.6)

# 表示
st.write(f"### {years}年後のあなたへの影響")
st.pyplot(fig)

st.info(f"現在の努力量「{effort}」を継続すると、{years}年後には現在の約 {outcome_curve[-1]:.1f} 倍の成果が得られる可能性があります。")
