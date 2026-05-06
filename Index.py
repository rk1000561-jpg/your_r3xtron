from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# 1. Home Route - Taaki link kholte hi "Active" dikhe
@app.route('/')
def home():
    return "✅ BGMI API Server is Active! Use /api/bgmi/YOUR_ID"

# 2. Main API Endpoint
@app.route('/api/bgmi/<uid>')
def get_user(uid):
    # RapidAPI URL
    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{uid}"
    
    # Aapki API Key
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518"
    }

    try:
        response = requests.get(url, headers=headers)
        # Agar status code 200 hai toh data return karega
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "ID not found or API error", "status": response.status_code}), response.status_code
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. Render Port Configuration
if __name__ == "__main__":
    # Render automatically environment variable se port uthata hai
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
