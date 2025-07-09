import os
import requests
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("GFW_EMAIL", "").strip()
PASSWORD = os.getenv("GFW_PASSWORD", "").strip()
LOGIN_URL = "https://api.resourcewatch.org/auth/login"

def get_gfw_token():
    if not EMAIL or not PASSWORD:
        raise ValueError("Credenciais ausentes. Verifique o .env")

    payload = {
        "email": EMAIL,
        "password": PASSWORD
    }

    try:
        response = requests.post(LOGIN_URL, json=payload)
        if response.status_code == 200:
            return response.json()["data"]["token"]
        else:
            print("Erro na autenticação:", response.status_code, response.text)
            return None
    except Exception as e:
        print("Erro de conexão:", str(e))
        return None
