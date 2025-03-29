import streamlit as st

# Streamlitページ設定
st.set_page_config(
    page_title="AI診断プラットフォーム",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Firebaseや質問生成関連のインポート
from firebase_config import db
from diagnosis_generator import generate_questions

def main():
    st.title("AI診断プラットフォーム")
    st.sidebar.header("設定")
    category = st.sidebar.selectbox("診断カテゴリ", ["性格診断", "適職診断", "恋愛傾向"])
    difficulty = st.sidebar.slider("難易度", 1, 3, 2)

    questions = generate_questions(category, num_questions=5)
    answers = []
    for i, question in enumerate(questions):
        answers.append(st.text_area(f"Q{i+1}: {question}", key=f"q{i}"))

    if st.button("診断を実行"):
        if all(answers):
            st.subheader("診断結果")
            st.write("診断結果を計算中...")
        else:
            st.warning("すべての質問に回答してください")

if __name__ == "__main__":
    main()
