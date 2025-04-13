import firebase_admin
from firebase_admin import credentials, firestore

# 初期化（1回だけ）
cred = credentials.Certificate("server-monitor-mcp-v2-firebase-adminsdk-fbsvc-a56f5d84be.json")
firebase_admin.initialize_app(cred)
db = firestore.client()