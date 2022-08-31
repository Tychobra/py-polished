__version__ = '0.0.1'

static_path = __path__[0] + "/static"

from .secure_ui import secure_ui
from .secure_server import secure_server
from .polished_config import polished_config
from .sign_out import sign_out
