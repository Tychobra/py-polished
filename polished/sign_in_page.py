from shiny import *

def sign_in_ui():
    
    out = ui.page_fluid(
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
        )
    )

    return out

def sign_in_server(input, output, session): 
    
    @reactive.Effect
    @reactive.event(input.submit_sign_in)
    def _():
        hold_email = input.email()
        hold_password = input.password()

        try:
            sign_in(hold_email, hold_password)
            print("sign in success")
            # if sign in is successful, redirect to app, else show error message
        except Exception as e:
            print("sign in error")
            print(e)
