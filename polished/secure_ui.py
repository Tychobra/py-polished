from shiny import App, render, ui, reactive
import hashlib

my_hash = hashlib.md5()

sign_in_ui = ui.page_fluid(
    ui.h2("Sign In"),
    ui.input_text(
        "email",
        "Email",
        value = ""
    ),
    ui.input_password(
        "password",
        "Password",
        value = ""
    ),
    ui.input_action_button(
        "submit_sign_in",
        "Sign In"
    ),
    ui.output_text_verbatim("sign_in_out")
)

def secure_ui(ui):
   
    def fun_out(request):
        
        polished_user = None
        hold_cookie = request.cookies.get("polished")

        if (hold_cookie != None):
            hashed_cookie = my_hash.update(hold_cookie.encode('utf-8'))
            
            try:
                polished_user = get_sessions(hashed_cookie)
            except:
                print("error getting session")
        
        if (polished_user == None):
            page_out = sign_in_ui
        else:
            page_out = ui
        
        return page_out

    return fun_out 

