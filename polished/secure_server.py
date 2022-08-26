from shiny import App, render, ui, reactive

from .sign_in_page import sign_in_server

def secure_server(server): 
    
    def fun_out(input, output, session):
        
        # if on sign in page return this
        out = sign_in_server(input, output, session)


        # if on app return the app server
        # out = server(input, output, server)

        return out

    return fun_out
    
