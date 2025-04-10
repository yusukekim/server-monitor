from flask import Flask, render_template, jsonify
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

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # hostを0.0.0.0にして他のデバイスからもアクセスできるように