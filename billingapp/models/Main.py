from billingapp.app import app
from flask_sqlalchemy import SQLAlchemy


class Main:
    def __init__(self):
        self.db = SQLAlchemy(app)


main = Main()
