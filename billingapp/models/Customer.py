from .Main import main
from .User import User
from flask_login import current_user


class Customer(main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    name = main.db.Column(main.db.String(200), nullable=False)
    address = main.db.Column(main.db.String(200), nullable=False)
    siret = main.db.Column(main.db.String(200))
    email = main.db.Column(main.db.String(200))
    phone = main.db.Column(main.db.String(200))
    enterprise_id = main.db.Column(main.db.Integer, main.db.ForeignKey("enterprise.id"))
    enterprise = main.db.relationship("Enterprise", backref="customer")

    def __init__(self, name, address, siret, email, phone):
        self.name = name
        self.address = address
        self.siret = siret
        self.email = email
        self.phone = phone

    @staticmethod
    def insert_customer(name, siret, email, phone, address):
        customer = Customer(name, address, siret, email, phone)
        User.query.get(current_user.id).enterprise[0].customer.append(customer)
        main.db.session.add(customer)
        main.db.session.commit()
        return customer.id

    def update_customer(self, name, siret, email, phone, address):
        self.name = name
        self.siret = siret
        self.email = email
        self.phone = phone
        self.address = address
        main.db.session.add(self)
        main.db.session.commit()

    def delete_customer(self):
        main.db.session.delete(self)
        main.db.session.commit()
