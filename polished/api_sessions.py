import requests
from ._polished import _polished

def get_sessions(app_name, hashed_cookie, api_key = _polished["api_key"]):
       
    res = requests.get(
        _polished["api_url"] + "/sessions",
        params = {
            "app_name": app_name,
            "hashed_cookie": hashed_cookie
        },
        auth = (api_key,"")
    )

    return res.json()
