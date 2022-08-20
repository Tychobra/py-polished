from shiny import App, render, ui
from polished import polished_config, secure_ui, secure_server
import yaml

app_config = None
with open("config.yml", "r") as stream:
    app_config = yaml.safe_load(stream)

polished_config(
    app_name = "polished_example_01",
    api_key = app_config["api_key"]
)

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny!"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt")
)



def server(input, output, session):
    
    print(session)
        
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

ui = secure_ui(app_ui)

server = secure_server(server)

app = App(ui, server)
