from shiny import reactive

from ._polished import _polished
from .sign_in_page import sign_in_server
from .api_sessions import get_sessions

def secure_server(server): 
    
    def fun_out(input, output, session):
        
        @reactive.Effect
        @reactive.event(input.hashed_cookie)
        def _():
            
            polished_user = None
            hold_cookie = input.hashed_cookie()

            print(f"server cookie: {hold_cookie}")

            if hold_cookie == "":   
                sign_in_server(input, output, session)
            else:
                
                try:
                    polished_user = get_sessions(
                        app_uid = _polished["app_uid"], 
                        hashed_cookie = hold_cookie, 
                        api_key = _polished["api_key"]
                    )

                except Exception as err:
                    print("server - error getting session")
                    print(err)
            
                print(f"server polished_user: {polished_user}")

                if polished_user == None:
                    sign_in_server(input, output, session)
                else:
                    server(input, output, session)

    return fun_out
