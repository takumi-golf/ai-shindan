import streamlit as st

st.title("AI診断プラットフォーム - 改良型インターフェース")

# 症状選択
st.header("症状について教えてください")
symptoms = st.multiselect(
    "当てはまる症状を選択してください",
    ["頭痛", "めまい", "吐き気", "発熱", "せき"]
)

# 症状の程度
st.header("症状の程度を教えてください")
headache_severity = st.slider("頭痛", 0, 5, step=1)
dizziness_severity = st.slider("めまい", 0, 5, step=1)
nausea_severity = st.slider("吐き気", 0, 5, step=1)

# 発症時期
onset = st.selectbox(
    "症状はいつ頃から始まりましたか？",
    ["今日", "昨日", "2-3日前", "1週間前", "1週間以上前"]
)

# 自由記述エリア（任意）
additional_info = st.text_area(
    "その他気になること（任意）",
    height=100
)

if st.button("診断する"):
    st.write("診断結果を計算中...")
