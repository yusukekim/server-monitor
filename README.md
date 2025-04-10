🚀　概要
このツールは、Pythonの Flask と psutil を用いて作成した
軽量なローカルサーバー監視ダッシュボードです。
	•	CPU使用率
	•	メモリ使用率
を リアルタイムでグラフ表示します（Chart.js使用）。

🔧 構成技術
Pyhon/Frask：Webサーバー
psuitil：リソース使用率取得
Chart.js：グラフ描写
HTML/JS：UI構築

📁 フォルダ構成
server-monitor/
├── app.py
├── requirements.txt
├── static/
│   └── main.js
├── templates/
│   └── index.html
└── README.md

今後の拡張アイデア
	•	Slack通知連携
	•	データの保存（CSV/SQLite）
	•	MCPによる文脈判断API
	•	複数端末のリソース収集

🧑‍💻 作者
	•	名前：kimuyuu
	•	職種：インフラ系エンジニア
	•	得意分野：ネットワーク／監視／セキュリティ
	•	趣味：ギターとラーメン🍜🎸