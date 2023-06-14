
class Config(object):
    SECRET_KEY = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GRAVATAR_CONFIG = {'size': 100, 'rating': 'g', 'default': 'retro', 'force_default': False, 'force_lower': False, 'use_ssl': False, 'base_url': None}
