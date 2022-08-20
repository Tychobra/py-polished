import requests


def get_sessions(app_name, hashed_cookie, api_key = __polished__["api_key"]):
    


    res = requests.get(
        __polished__["api_url"] + "/sessions",
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