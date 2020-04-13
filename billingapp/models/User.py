from .Main import main
from flask_login import UserMixin
import hashlib
import os


class User(UserMixin, main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    email = main.db.Column(main.db.String(200), nullable=False, unique=True)
    first_name = main.db.Column(main.db.String(200))
    last_name = main.db.Column(main.db.String(200))
    key = main.db.Column(main.db.Binary, nullable=False)
    salt = main.db.Column(main.db.Binary)

    def __init__(self, email, password, first_name, last_name):
        self.email = email
        self.salt = os.urandom(32)
        self.key = self.hash_password(password)
        self.first_name = first_name
        self.last_name = last_name

    def get_id(self):
        return self.id

    def hash_password(self, password):
        salt = self.salt

        if type(salt) is not bytes:
            salt = salt.encode('utf-8')

        key = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 100000)

        return key

    def update_user_infos(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        main.db.session.add(self)
        main.db.session.commit()

    def update_user_password(self, current_password, new_password):
        if self.hash_password(current_password) == self.key:
            self.key = self.hash_password(new_password)
            main.db.session.add(self)
            main.db.session.commit()
            return True
        else:
            return False
