from .Main import main


class Product(main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    name = main.db.Column(main.db.String, nullable=False)
    product_code = main.db.Column(main.db.String, nullable=False)
    price_ht = main.db.Column(main.db.Integer)

    def __init__(self, name, product_code, price_ht):
        self.name = name
        self.product_code = product_code
        self.price_ht = price_ht

    @staticmethod
    def insert_product(name, product_code, price_ht):
        product = Product(name, product_code, price_ht)
        main.db.session.add(product)
        main.db.session.commit()
        return product.id

    def update_product(self, name, product_code, price_ht):
        self.name = name
        self.product_code = product_code
        self.price_ht = price_ht
        main.db.session.add(self)
        main.db.session.commit()

    def delete_product(self):
        main.db.session.delete(self)
        main.db.session.commit()

