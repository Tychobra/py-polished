import requests
from .polished_config import _polished

def get_sessions(app_name, hashed_cookie, api_key = _polished["api_key"]):
       
    res = requests.post(
        _polished["api_url"] + "/",
        params = {
            "app_name": app_name,
            "hashed_cookie": hashed_cookie
        },
        auth = {
            "user": api_key,
            "password": ""
        }
    )

    return res.json()