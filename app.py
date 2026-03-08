from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='static')
CORS(app)

N8N_BASE_URL = os.environ.get("N8N_BASE_URL", "http://localhost:5678")
API_KEY = os.environ.get("N8N_API_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5M2U2NGY0MC1iZWE2LTRkODgtODg4YS1hY2YwOGIwYWVlMDIiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzcyODc5NTM1LCJleHAiOjE3NzU0NDgwMDB9.udSwTo5z5TtjirEv_tPRqdiHmVbcm_zACM7exATs5Kg")

HEADERS = {
    "X-N8N-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

@app.route("/")
def index():
    return send_from_directory("static", "try.html")

@app.route("/api/workflows")
def get_workflows():
    try:
        response = requests.get(f"{N8N_BASE_URL}/api/v1/workflows", headers=HEADERS)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/workflows/<workflow_id>")
def get_workflow(workflow_id):
    try:
        response = requests.get(f"{N8N_BASE_URL}/api/v1/workflows/{workflow_id}", headers=HEADERS)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/executions")
def get_executions():
    try:
        response = requests.get(f"{N8N_BASE_URL}/api/v1/executions?limit=50", headers=HEADERS)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("🚀 n8n Dashboard running at http://localhost:5000")
    app.run(debug=True, port=5000)

