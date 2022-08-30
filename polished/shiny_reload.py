



async def shiny_reload(session, page = None):
    """reload the shiny server session"""
    await session.send_custom_message(
        "shiny_reload", 
        message = {"page": page}
    )
