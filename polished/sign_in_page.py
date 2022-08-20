from shiny import render, ui, reactive

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