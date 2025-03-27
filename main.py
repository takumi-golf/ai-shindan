import streamlit as st
import numpy as np
from diagnosis_generator import generate_questions
from sentence_transformers import SentenceTransformer
from firebase_config import db  # 追加
from firebase_admin import firestore  # 追加
import streamlit as st
import os

# Check if running on Netlify
is_netlify = os.environ.get('NETLIFY') == 'true'

if is_netlify:
    # Netlify specific settings
    st.set_page_config(page_title="AI診断プラットフォーム", layout="wide")
else:
    # Local development settings
    st.set_page_config(page_title="AI診断プラットフォーム (開発中)", layout="wide")

# Rest of your Streamlit app code...



# Streamlitページ設定
st.set_page_config(page_title="AI診断プラットフォーム", layout="wide")

# SentenceTransformerモデル初期化
model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

def analyze_answers(answers):
    answer_embeddings = model.encode(answers)
    average_embedding = np.mean(answer_embeddings, axis=0)
    
    # 仮の性格タイプ分類
    personality_types = ["外向的", "内向的", "論理的", "感情的", "冒険的"]
    
    # ランダム選択（実際はベクトル比較を推奨）
    result = np.random.choice(personality_types)
    
    return {
        "primary_type": result,
        "confidence": float(np.random.rand()),
        "vector": average_embedding.tolist()
    }

# サイドバー設定
with st.sidebar:
    st.header("設定")
    category = st.selectbox("診断カテゴリ", ["性格診断", "適職診断", "恋愛傾向"])
    difficulty = st.slider("難易度", 1, 3, 2)

# メインコンテンツ
st.title("AI診断プラットフォーム")
questions = generate_questions(category, num_questions=5)

answers = []
for i, question in enumerate(questions):
    answers.append(st.text_area(f"Q{i+1}: {question}", key=f"q{i}"))

if st.button("診断を実行"):
    if all(answers):  # 全回答チェック
        results = analyze_answers(answers)
        st.subheader("診断結果")
        st.write(f"あなたは【{results['primary_type']}】タイプです")
        st.write(f"信頼度: {results['confidence']:.2f}")
        
        # Firebase保存処理
        try:
            doc_ref = db.collection('diagnoses').document()
            doc_ref.set({
                'answers': answers,
                'result': results['primary_type'],
                'confidence': results['confidence'],
                'timestamp': firestore.SERVER_TIMESTAMP
            })
            st.success("診断結果を保存しました！")
        except Exception as e:
            st.error(f"保存に失敗しました: {str(e)}")
    else:
        st.warning("すべての質問に回答してください")
