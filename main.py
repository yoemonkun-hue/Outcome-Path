import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# ページ設定
st.set_page_config(page_title="Future Outcomes Simulator", layout="centered") # スマホで見やすい中央寄せ

st.title("🚀 Future Outcomes Simulator Pro")

# --- メイン画面に設定を表示（スマホ対策） ---
st.header("⚙️ 設定")
col_input1, col_input2 = st.columns(2)

with col_input1:
    effort = st.slider("今日の努力量 (0-100)", 0, 100, 70)
    years = st.slider("期間 (年)", 1, 10, 5)

with col_input2:
    consistency = st.slider("継続率 (%)", 1, 100, 90) / 100
    target_goal = st.number_input("目標とする成果レベル", value=50.0)

st.markdown("---")

# 計算ロジック
days = np.linspace(0, years, int(years * 365))
outcomes = (1 + (effort / 100) * consistency) ** days - 1
final_score = outcomes[-1]

# グラフと結果の表示
st.subheader("📊 成長予測グラフ")
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(days, outcomes, color='#FF4B4B', linewidth=3, label='Your Growth')
ax.axhline(y=target_goal, color='gray', linestyle='--', label='Target Goal')
ax.set_xlabel("Years")
ax.set_ylabel("Accumulated Outcomes")
ax.grid(True, linestyle=':', alpha=0.6)
st.pyplot(fig)

# 結果のまとめ
st.subheader("📝 シミュレーション結果")
st.metric("最終的な成果", f"{final_score:.1f} 倍")

if final_score >= target_goal:
    reach_day_idx = np.where(outcomes >= target_goal)[0][0]
    reach_year = days[reach_day_idx]
    st.success(f"✅ 目標達成！ 約 {reach_year:.1f} 年で目標に届きます。")
else:
    st.warning(f"⚠️ 目標まであと {(target_goal - final_score):.1f} 足りません。")

# 解説セクション（アスタリスクを修正済み）
st.markdown("---")
st.header("🔍 数値が持つ「人生の意味」")
tab1, tab2, tab3 = st.tabs(["🔥 努力量", "⌛ 継続率", "📈 成長"])

with tab1:
    st.write("この数値は、あなたが今日「どれだけ自分に誇りを持てる行動をしたか」を表します。")
with tab2:
    st.write("「100の努力を1日」より「10の努力を10日」続ける方が、複利の魔法が強く効きます。完璧主義を捨てて、0点の日を作らないことがコツです。")
with tab3:
    st.write(f"最終成果が {final_score:.1f} 倍になるのは、知識やスキルが複利で増えるからです。")

st.caption("©️ 2026 Future Outcomes Simulator - 継続は力なり")
