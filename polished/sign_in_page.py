import hashlib
from shiny import *

from ._polished import _polished
from .sign_in import sign_in

my_hash = hashlib.md5()

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
    def _():
        hold = input.check_jwt()
        
        breakpoint()
        try:

            hashed_cookie = hashlib.md5(hold["cookie"].encode('utf-8'))
            hashed_cookie = hashed_cookie.digest()
            
            user = sign_in(
                app_uid = _polished["app_uid"], 
                email = hold['email'], 
                password = hold['password'],
                hashed_cookie = hashed_cookie
            )
            
            

            #if (user['error']) {
            #  
            #}
            print("sign in success")
            print(user)
            
            # if sign in is successful, redirect to app, else show error message
        except Exception as e:
            print("sign in error")
            print(e)
