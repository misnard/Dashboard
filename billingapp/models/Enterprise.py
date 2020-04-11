from .Main import main


class Enterprise(main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    user_id = main.db.Column(main.db.Integer, main.db.ForeignKey("user.id"))
    user = main.db.relationship("User", backref="enterprise")
    name = main.db.Column(main.db.String(200), nullable=False)
    address = main.db.Column(main.db.String(200), nullable=False)
    city = main.db.Column(main.db.String(200))
    postal_code = main.db.Column(main.db.String(200))
    phone = main.db.Column(main.db.String(200))
    email = main.db.Column(main.db.String(200))
    bank_infos = main.db.Column(main.db.String(200))
    siret = main.db.Column(main.db.String(200))

    def __init__(self, name, address, city, postal_code, phone, email, bank_infos, siret):
        self.name = name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.phone = phone
        self.email = email
        self.bank_infos = bank_infos
        self.siret = siret

    @staticmethod
    def insert_enterprise(name, address, city, postal_code, phone, email, bank_infos, siret):
        enterprise = Enterprise(name, address, city, postal_code, phone, email, bank_infos, siret)

        main.db.session.add(enterprise)
        main.db.session.commit()

    def update_enterprise(self, name, address, city, postal_code, phone, email, bank_infos, siret):
        self.name = name
        self.address = address
        self.city = city
        self.postal_code = postal_code
        self.phone = phone
        self.email = email
        self.bank_infos = bank_infos
        self.siret = siret
        main.db.session.add(self)
        main.db.session.commit()
