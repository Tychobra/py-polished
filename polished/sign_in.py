import requests
from ._polished import _polished

def sign_in(app_uid, email, password, api_key = _polished["api_key"]):
       
    res = requests.post(
        _polished["api_url"] + "/sign-in-email",
        params = {
            "app_uid": app_uid,
            "email": email,
            "password": password
        },
        auth = (api_key, "")
    )

    return res.json()
