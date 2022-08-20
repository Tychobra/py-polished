
polished = {
  "api_url": "https://auth-api.polished.tech/v1",
  "app_name": "",
  "api_key": ""
}

def polished_config(app_name, api_key):
    global polished
    
    polished["app_name"] = app_name
    polished["api_key"] = api_key

