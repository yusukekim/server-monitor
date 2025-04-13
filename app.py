from flask import Flask, render_template, jsonify, request
import psutil

app = Flask(__name__)

# メインページ表示
@app.route("/")
def index():
    return render_template("index.html")

# リソースデータ取得API
@app.route("/api/status")
def api_status():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    return jsonify({"cpu": cpu, "mem": mem})

# 文脈保存API /mcp/context（POST）

def save_context():
    data = request.json
    user = data.get("user")
    context = {
        "cpu_threshold": data["alert"]["cpu_threshold"],
        "mem_threshold": data["alert"]["mem_threshold"],
        "duration": data.get("duration", 300)
    }
    db.collection("contexts").document(user).set(context)
    return {"status": "ok", "message": f"context saved for user: {user}"}

# 🟠 文脈に基づくステータスチェック
@app.route("/mcp/status")
def check_status():
    user = request.args.get("user")
    doc = db.collection("contexts").document(user).get()
    if not doc.exists:
        return {"error": "no context found"}, 404

    context = doc.to_dict()
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent

    alert = cpu > context["cpu_threshold"] or mem > context["mem_threshold"]
    return {
        "cpu": cpu,
        "mem": mem,
        "alert": alert,
        "threshold": context
    }

from flask import request  # すでにあるかもやけど、念のため確認！

@app.route("/mcp/context", methods=["POST"])
def save_context():
    data = request.json
    user = data.get("user")
    context = {
        "cpu_threshold": data["alert"]["cpu_threshold"],
        "mem_threshold": data["alert"]["mem_threshold"],
        "duration": data.get("duration", 300)
    }
    from firebase_util import db  # firebase_util.py からdbをインポート
    db.collection("contexts").document(user).set(context)
    return {"status": "ok", "message": f"context saved for user: {user}"}

if __name__ == "__main__":
    app.run(debug=True, port=5001) # 5000ポートから変更