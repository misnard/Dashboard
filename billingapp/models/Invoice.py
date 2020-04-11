from .Main import main
from .Customer import Customer
from .Item import Item
from .Product import Product
from .InvoiceStatus import InvoiceStatus


class Invoice(main.db.Model):
    id = main.db.Column(main.db.Integer, primary_key=True)
    description = main.db.Column(main.db.String(200))
    amount = main.db.Column(main.db.Integer)
    status = main.db.Column(main.db.Enum(InvoiceStatus), nullable=False)
    customer = main.db.relationship("Customer", backref="invoice")
    customer_id = main.db.Column(main.db.Integer, main.db.ForeignKey("customer.id"))
    vat = main.db.Column(main.db.Integer, default=0)

    def __init__(self, description, amount, status, customer_id):
        self.description = description
        self.amount = amount
        self.status = status
        self.customer = customer_id

    def total(self):
        total = 0
        for i in self.item:
            total += i.item_total()
        return total

    def get_customer(self):
        return Customer.query.get(self.customer_id)

    @staticmethod
    def insert_invoice(name, customer, items):
        invoice_items = []
        invoice_total = 0

        for item in items:
            invoice_product = Item(item[0], item[1])
            invoice_items.append(invoice_product)
            invoice_total += int(Product.query.filter_by(product_code=item[0]).one().price_ht) * int(item[1])

        invoice = Invoice(name, invoice_total, InvoiceStatus["pending"], Customer.query.get(customer))
        invoice.item.extend(invoice_items)
        main.db.session.add(invoice)
        main.db.session.commit()
        return invoice.id

    def delete_invoice(self):
        main.db.session.delete(self)
        main.db.session.commit()
