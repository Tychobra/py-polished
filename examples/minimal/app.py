from imp import PKG_DIRECTORY
from shiny import App, render, ui, reactive
from polished import polished_config, secure_ui, secure_server, sign_out, static_path 
import yaml


app_config = None
with open("config.yml", "r") as stream:
    app_config = yaml.safe_load(stream)

polished_config(
    app_name = "polished_example_01",
    api_key = app_config["api_key"]
)

app_ui = ui.page_fluid(
    ui.row(
      ui.column(
        6,
        ui.h2("Hello Shiny!")
      ),
      ui.column(
        6,
        ui.input_action_button(
            "sign_out",
            "Sign Out"
        )
      )
    ),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
    ui.tags.script(src="polished/js/auth_main.js"),
    ui.tags.script("auth_main('')")
)

def app_server(input, output, session):
    
    @reactive.Effect
    @reactive.event(input.sign_out)
    async def _():
        await sign_out(session)
        
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

ui = secure_ui(app_ui)

server = secure_server(app_server)

app = App(ui, server, static_assets=polished_static)
