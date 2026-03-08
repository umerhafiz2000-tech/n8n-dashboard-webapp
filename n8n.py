import requests

N8N_BASE_URL = "http://localhost:5678"  # or your n8n host
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI5M2U2NGY0MC1iZWE2LTRkODgtODg4YS1hY2YwOGIwYWVlMDIiLCJpc3MiOiJuOG4iLCJhdWQiOiJwdWJsaWMtYXBpIiwiaWF0IjoxNzcyODc5NTM1LCJleHAiOjE3NzU0NDgwMDB9.udSwTo5z5TtjirEv_tPRqdiHmVbcm_zACM7exATs5Kg"

headers = {
    "X-N8N-API-KEY": API_KEY,
    "Content-Type": "application/json"
}

response = requests.get(f"{N8N_BASE_URL}/api/v1/workflows", headers=headers)

if response.status_code == 200:
    workflows = response.json()
    for wf in workflows.get("data", []):
        print(f"ID: {wf['id']} | Name: {wf['name']} | Active: {wf['active']}")
else:
    print(f"Error: {response.status_code} - {response.text}")