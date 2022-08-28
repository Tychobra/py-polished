import requests
from ._polished import _polished

def sign_in(app_uid, email, password, hashed_cookie, api_key = _polished["api_key"]):
    
    res = requests.post(
        _polished["api_url"] + "/sign-in-email",
        json = {
            "app_uid": app_uid,
            "email": email,
            "password": password,
            "hashed_cookie": hashed_cookie,
            "is_invite_required": False
        },
        auth = (api_key, "")
    )

    return res
