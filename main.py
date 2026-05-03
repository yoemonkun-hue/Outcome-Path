import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 1. ページ設定（デザインを広く、アプリっぽく）
st.set_page_config(page_title="Future Outcomes Simulator", layout="wide")

st.title("🚀 Future Outcomes Simulator Pro")
st.markdown("---")

# 2. サイドバーでの入力項目
with st.sidebar:
    st.header("⚙️ 設定")
    effort = st.slider("今日の努力量 (0-100)", 0, 100, 70)
    years = st.slider("期間 (年)", 1, 10, 5)
    
    st.subheader("💡 オプション")
    # 挫折シミュレーション
    consistency = st.slider("継続率 (%)", 1, 100, 90) / 100
    # 目標設定
    target_goal = st.number_input("目標とする成果レベル", value=50.0)

# 3. 計算ロジック
days = np.linspace(0, years, years * 365)
# 努力が複利で効いてくる計算式（継続率を加味）
outcomes = (1 + (effort / 100) * consistency) ** days - 1

# 4. メイン画面のレイアウト
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 成長予測グラフ")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(days, outcomes, color='#FF4B4B', linewidth=3, label='Your Growth')
    ax.axhline(y=target_goal, color='gray', linestyle='--', label='Target Goal')
    ax.set_xlabel("Years", fontsize=12)
    ax.set_ylabel("Accumulated Outcomes", fontsize=12)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.legend()
    st.pyplot(fig)

with col2:
    st.subheader("📝 シミュレーション結果")
    final_score = outcomes[-1]
    
    # 目標達成の判定
    st.metric("最終的な成果", f"{final_score:.1f} 倍")
    
    if final_score >= target_goal:
        # 目標達成までの年数を逆算
        reach_day_idx = np.where(outcomes >= target_goal)[0][0]
        reach_year = days[reach_day_idx]
        st.success(f"✅ 目標達成！ 約 {reach_year:.1f} 年で目標に届きます。")
    else:
        st.warning(f"⚠️ 目標まであと {(target_goal - final_score):.1f} 足りません。努力量か継続率を上げてみましょう。")

    st.info(f"現在の努力量「{effort}」と継続率「{consistency*100:.0f}%」を維持すると、5年後には爆発的な成長が期待できます。")

# 5. フッター
st.markdown("---")
st.caption("©️ 2026 Future Outcomes Simulator - 継続は力なり")
