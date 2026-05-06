from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# 1. Home Route (Taaki 404 na aaye)
@app.route('/')
def home():
    return "✅ BGMI API Server is Active! Use /api/bgmi/YOUR_ID"

# 2. Main API Endpoint
@app.route('/api/bgmi/<uid>')
def get_user(uid):
    # RapidAPI URL
    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{uid}"
    
    # Aapki API Key (Fix kar di hai)
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518"
    }

    try:
        response = requests.get(url, headers=headers)
        # Check agar response sahi hai
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "ID not found or API issue", "status": response.status_code}), response.status_code
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. Render ke liye Port setup
if __name__ == "__main__":
    # Render automatically port assign karta hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
