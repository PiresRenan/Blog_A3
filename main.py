# main.py
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_gravatar import Gravatar
from config.configuration import Config
from model.db import User, db
from routes.main_routes import routes

app = Flask(__name__)
app.config.from_object(Config)
ckeditor = CKEditor(app)
Bootstrap(app)
gravatar = Gravatar(app, **app.config['GRAVATAR_CONFIG'])
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


app.register_blueprint(routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
