from .shiny_reload import shiny_reload


async def sign_out(session): 
    await shiny_reload(session, page="sign_in")
