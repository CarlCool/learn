from config import configs
import os
COOKIE_NAME = 'awesession'
_COOKIE_KEY = configs.session.secret
print(_COOKIE_KEY)
path = os.path.dirname(__file__)
print(path)