import requests

from ._polished import _polished

def polished_config(app_name, api_key):
    global _polished
    
    app_out = None
    
    res = requests.get(
        _polished["api_url"] + "/apps",
        params = {
            "app_name": app_name
        },
        auth = (api_key,"")
        
    )

    app_out = res.json()
    
    _polished["app_name"] = app_out["app_name"]
    _polished["app_uid"] = app_out["uid"]
    _polished["api_key"] = api_key

