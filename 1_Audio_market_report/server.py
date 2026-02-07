from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS
import requests

# templatesフォルダにあるHTMLを使えるように設定
app = Flask(__name__, template_folder='templates')
CORS(app) # フロントエンド(HTML)からのアクセスを許可

MINARA_API_URL = "https://api.minara.ai/v1/developer/chat"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate_report', methods=['POST'])
def generate_report():
    """
    Proxy request to Minara API and stream the response.
    """
    try:
        data = request.json
        user_text = data.get('text')
        user_api_key = request.headers.get('X-Minara-Key')

        if not user_api_key:
            return jsonify({"error": "API Key is required."}), 401
        
        if not user_text:
            return jsonify({"error": "Input text is empty."}), 400

        print(f"[INFO] Generating report for: {user_text[:50]}...")

        headers = {
            "Authorization": f"Bearer {user_api_key}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "mode": "fast",
            "stream": True,
            "message": {
                "role": "user",
                "content": user_text
            }
        }

        response = requests.post(MINARA_API_URL, headers=headers, json=payload, stream=True)
        
        if not response.ok:
            return jsonify({
                "error": f"Upstream API Error: {response.status_code}",
                "details": response.text
            }), response.status_code

        def generate():
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    yield chunk

        return Response(generate(), content_type=response.headers.get('Content-Type'))

    except Exception as e:
        print(f"[ERROR] Internal Server Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting server at http://localhost:5000")
    app.run(host='0.0.0.0', port=5000)