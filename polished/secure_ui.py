import hashlib
from shiny import ui as ui_

from ._polished import _polished
from .sign_in_page import sign_in_ui
from .api_sessions import get_sessions
from .admin_app import admin_ui


def secure_ui(ui):
   
    def fun_out(request):
        
        polished_user = None
        hold_cookie = request.cookies.get("polished")
        query_page = request.query_params.get("page", None)
        hashed_cookie = ""
        print(f"hold_cookie: {hold_cookie}")
        if (hold_cookie != None or hold_cookie == ""):
            hashed_cookie = hashlib.md5(hold_cookie.encode('utf-8'))
            hashed_cookie = hashed_cookie.hexdigest()
            
            try:
                polished_user = get_sessions(
                    app_uid = _polished["app_uid"],
                    hashed_cookie = hashed_cookie, 
                    api_key = _polished["api_key"]
                )
            except Exception as err:
                print("ui - error getting session")
                print(err)
        
        print(f"ui polished_user: {polished_user}")

        script_out = ui_.tags.script("$(document).on('shiny:sessioninitialized', function () {Shiny.setInputValue('hashed_cookie', '" + hashed_cookie + "', {'priority': 'event'});})")

        if (polished_user == None):
            page_out = ui_.TagList(
                sign_in_ui(),
                script_out
            )
            
        else:

            if (query_page == None):
                page_out = ui_.TagList(
                    ui,
                    script_out
                )
                
            else:
                page_out = ui_.TagList(
                    admin_ui(),
                    script_out  
                )
                  
        
        return page_out

    return fun_out 

