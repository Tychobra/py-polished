import requests
from ._polished import _polished

def get_sessions(app_uid, hashed_cookie, api_key = _polished["api_key"]):
       
    res = requests.get(
        _polished["api_url"] + "/sessions",
        params = {
            "app_uid": app_uid,
            "hashed_cookie": hashed_cookie
        },
        auth = (api_key,"")
    )

    
    out = res.json()

    if len(out) == 0:
        out = None 
    
    return out
