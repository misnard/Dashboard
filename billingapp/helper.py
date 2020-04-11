from .models.Invoice import Invoice
from .models.Enterprise import Enterprise
from .models.Customer import Customer
from .models.Product import Product
from .models.InvoiceConfig import InvoiceConfig
from .models.User import User
from .models.InvoiceStatus import InvoiceStatus
from flask_login import current_user


def get_invoices():
    return Invoice.query.all()


def get_pending_invoices():
    return Invoice.query.filter_by(status=InvoiceStatus(0)).all()


def get_invoice(invoice_id):
    return Invoice.query.get(invoice_id)


def get_enterprise_infos():
    return Enterprise.query.one()


def get_customers():
    return Customer.query.all()


def get_products():
    return Product.query.all()


def insert_invoice(name, customer, items):
    if name and customer and len(items) > 0:
        return Invoice.insert_invoice(name, customer, items)


def remove_invoice(invoice_id):
    invoice = Invoice.query.get(invoice_id)
    invoice.delete_invoice()


def get_invoice_config(key, enterprise_id):
    return InvoiceConfig.get_config_value(key, enterprise_id)


def get_invoice_configs():
    return InvoiceConfig


def get_user(email):
    return User.query.filter_by(email=email).first()


def get_customer(customer_id):
    return Customer.query.get(customer_id)


def insert_customer(name, siret, email, phone, address):
    if name and email and address:
        return Customer.insert_customer(name, siret, email, phone, address)


def update_customer(customer_id, name, siret, email, phone, address):
    if customer_id and name and email and address:
        customer = Customer.query.get(customer_id)
        return customer.update_customer(name, siret, email, phone, address)


def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    customer.delete_customer()


def get_product(product_id):
    return Product.query.get(product_id)


def insert_product(name, product_code, price_ht):
    if name and product_code and price_ht:
        return Product.insert_product(name, product_code, price_ht)


def update_product(product_id, name, product_code, price_ht):
    if product_id and name and product_code and price_ht:
        product = Product.query.get(product_id)
        return product.update_product(name, product_code, price_ht)


def delete_product(product_id):
    product = Product.query.get(product_id)
    product.delete_product()


def update_enterprise(name, address, city, postal_code, phone, email, siret, bank_infos):
    if name and address and city and postal_code and siret and bank_infos:
        enterprise = Enterprise.query.filter_by(user_id=current_user.id).one()
        enterprise.update_enterprise(name, address, city, postal_code, phone, email, bank_infos, siret)
