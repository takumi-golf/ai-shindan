import firebase_admin
from firebase_admin import credentials, firestore  # firestoreを追加

# 認証情報の初期化
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Firestoreクライアントの初期化
db = firestore.client()

# Firebaseの設定や関数をここに追加
def get_user_data(user_id):
    doc_ref = db.collection('users').document(user_id)
    doc = doc_ref.get()
    return doc.to_dict() if doc.exists else None

def save_diagnosis_result(user_id, result):
    doc_ref = db.collection('diagnosis_results').document(user_id)
    doc_ref.set(result)
