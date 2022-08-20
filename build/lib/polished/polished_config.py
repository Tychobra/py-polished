
__polished__ = {
  "api_url": "https://auth-api.polished.tech/v1",
  "app_name": "",
  "api_key": ""
}

def polished_config(app_name, api_key):
    global __polished__
    
    __polished__.app_name = app_name
    __polished__.api_key = api_key

