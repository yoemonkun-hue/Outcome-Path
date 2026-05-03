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
# --- 以下、説明用セクションの追加コード ---

st.markdown("---")
st.header("🔍 数値が持つ「人生の意味」")

tab1, tab2, tab3 = st.tabs(["🔥 努力量とは", "⌛ 継続率の真実", "📈 指数関数的な成長"])

with tab1:
    st.subheader("今日の努力量 (0-100)")
    st.write("""
    この数値は、あなたが今日「どれだけ自分に誇りを持てる行動をしたか」を表します。
    * **0〜30:** 現状維持。休息も大切ですが、変化は起きにくい状態です。
    * **31〜70:** 着実な一歩。習慣化ができ始めており、土台を作っている時期です。
    * **71〜100:** 限界突破。コンフォートゾーンを抜け出し、未来を強制的に変えている状態です。
    """)

with tab2:
    st.subheader("継続率 (%)")
    st.write("""
    「100の努力を1日」するよりも、「10の努力を10日」続ける方が、このシミュレーター（人生）では大きな意味を持ちます。
    継続率が下がると、複利の魔法が解けてしまい、グラフはただの直線に近づきます。
    **「完璧主義を捨てて、0点の日を作らないこと」**が、この数値を高く保つコツです。
    """)

with tab3:
    st.subheader("累積成果 (Accumulated Outcomes)")
    st.write(f"""
    最終的な成果が **{final_score:.1f}倍** になっているのは、知識やスキルが「複利」で増えるからです。
    最初は変化が見えませんが、ある地点（ティッピングポイント）を超えると、自分でも驚くような急成長が始まります。
    グラフの後半の急上昇は、あなたが今日投げ出さなかった結果として現れる未来の姿です。
    """)
