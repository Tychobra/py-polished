from shiny import App, render, ui, reactive


def secure_server(server): 
    
    def fun_out(input, output, session):
    
        @reactive.Calc
        @reactive.event(input.submit_sign_in)
        def sign_in_r(): 
            print(server)
            return input.submit_sign_in()
    
        @output
        @render.text
        def sign_in_out():
            return f"hi {sign_in_r()}"


    return fun_out
