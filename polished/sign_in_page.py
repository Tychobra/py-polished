import hashlib
from shiny import *

from ._polished import _polished
from .sign_in import sign_in
from .shiny_reload import shiny_reload


def sign_in_ui():
    
    out = ui.page_fluid(
        ui.h2("Sign In"),
        ui.input_text(
            "sign_in_email",
            "Email",
            value = ""
        ),
        ui.input_password(
            "sign_in_password",
            "Password",
            value = ""
        ),
        ui.tags.button(
             "Sign In",
            id = "sign_in_submit"
        ),
        # TODO: the cookie when the sign in is attempted
        ui.tags.script(src = "https://cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js"),
        ui.tags.script(src = "js/auth_main.js"),
        ui.tags.script("auth_main('')")
    )

    return out

def sign_in_server(input, output, session): 
    
    @reactive.Effect
    @reactive.event(input.check_jwt)
    async def _():
        hold = input.check_jwt()
        
        try:
            
            hashed_cookie = hashlib.md5(hold["cookie"].encode('utf-8'))
            hashed_cookie = hashed_cookie.hexdigest()

            sign_in_res = sign_in(
                app_uid = _polished["app_uid"], 
                email = hold['email'], 
                password = hold['password'],
                hashed_cookie = hashed_cookie,
                api_key = _polished["api_key"]
            )
            

            if (sign_in_res.status_code == 200):
                print("sign in success")
                # update the url

                await shiny_reload(session)
            else:
                print("sign in error")
                print(sign_in_res.json())    
             
            
        except Exception as e:
            print("sign in error catch")
            print(e)
