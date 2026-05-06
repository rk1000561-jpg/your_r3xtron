from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Basic Route
@app.route('/')
def home():
    return "✅ BGMI API Server is Active! Use /api/bgmi/YOUR_ID"

# Dynamic Endpoint
@app.route('/api/bgmi/<uid>')
def get_user(uid):
    # Aapka RapidAPI URL
    url = f"https://id-game-checker.p.rapidapi.com/bgmi/{uid}"
    
    # Headers mein aapki key already hai
    headers = {
        "x-rapidapi-host": "id-game-checker.p.rapidapi.com",
        "x-rapidapi-key": "4031d8fca9mshd856dbf4ba5f5e5p1ad3bejsnd6dbde6aa518"
    }

    try:
        response = requests.get(url, headers=headers)
        # Agar response valid hai toh JSON return karega
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ye line Vercel ko server start karne mein help karti hai
if __name__ == "__main__":
    app.run(debug=True)
