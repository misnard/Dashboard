from .Main import main
from .Product import Product


class Item(main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    product_code = main.db.Column(main.db.String, nullable=False)
    qty = main.db.Column(main.db.Integer)
    invoice = main.db.relationship("Invoice", backref=main.db.backref("item", lazy='dynamic'))
    invoice_id = main.db.Column(main.db.Integer, main.db.ForeignKey("invoice.id"))

    def __init__(self, product_code, qty):
        self.product_code = product_code
        self.qty = qty

    def session_infos(self):
        return Product.query.filter_by(product_code=self.product_code).one()

    def item_total(self):
        return Product.query.filter_by(product_code=self.product_code).one().price_ht * self.qty

