import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Firebaseの設定や関数をここに追加
def get_user_data(user_id):
    doc_ref = db.collection('users').document(user_id)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def save_diagnosis_result(user_id, result):
    doc_ref = db.collection('diagnosis_results').document(user_id)
    doc_ref.set(result)

# 他のFirebase関連の関数をここに追加