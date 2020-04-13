from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()

login_manager.init_app(app)
CSRFProtect().init_app(app)
app.config.from_object('config')
