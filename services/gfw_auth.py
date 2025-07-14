import os
import requests
from dotenv import load_dotenv
from requests.exceptions import Timeout

load_dotenv()

LOGIN_URL = "https://api.resourcewatch.org/auth/login"
_token_cache = None

def _get_credentials_to_payload () -> dict: 

    email = os.getenv("GFW_EMAIL", "").strip()
    password = os.getenv("GFW_PASSWORD", "").strip()
    if not email or not password:
        raise ValueError("Missing credentials. Check your .env")
    payload = {"email": email, "password": password}
    return payload


def get_gfw_token(force_refresh=False):
    global _token_cache
    if _token_cache and not force_refresh:
        return _token_cache

    _payload = _get_credentials_to_payload()
    
    try:
        response = requests.post(LOGIN_URL, json=_payload, timeout=5)
        response.raise_for_status()
        if response.status_code == 200:
            _token_cache = response.json()["data"]["token"]
            return _token_cache
        else: 
            print(f"[ERROR] Login failed ({response.status_code}): {response.text}")
            return None
    except Timeout:
        print("[ERROR] Login request timed out after 5 seconds.")
        return None
    except Exception as e:
        print(f"[ERROR] Could not connect to GFW: {e}")
        return None
