import hashlib

from .sign_in_page import sign_in_ui
from .api_sessions import get_sessions

my_hash = hashlib.md5()


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
            page_out = sign_in_ui()
        else:
            page_out = ui
        
        return page_out

    return fun_out 

