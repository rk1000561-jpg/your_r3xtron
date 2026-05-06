from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ BGMI API Server is Active! Use /api/bgmi/YOUR_ID"

@app.route('/api/bgmi/<uid>')
def get_user(uid):
    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{uid}"
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518"
    }
    try:
        response = requests.get(url, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
