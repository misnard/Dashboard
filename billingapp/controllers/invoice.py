from billingapp import app
import numpy as np
from flask_login import login_required
from flask import render_template, redirect, request
from billingapp.helper import get_invoices, get_customers, get_invoice, get_enterprise_infos, get_invoice_config, \
    get_products, remove_invoice, insert_invoice

""" Crud Invoice (R) """


@app.route('/invoices/')
@login_required
def invoices():
    return render_template('invoices.html', invoices=get_invoices(), customers=get_customers(), products=get_products(),
                           enterprise=get_enterprise_infos())


@app.route('/invoice/<invoice_id>/')
@login_required
def invoice(invoice_id):
    print(get_invoice(invoice_id).item)
    return render_template("invoice.html", invoice=get_invoice(invoice_id), enterprise_infos=get_enterprise_infos(),
                           invoice_config=get_invoice_config)


""" Crud Invoice (C) """


@app.route("/invoice/add/", methods=['GET', 'POST'])
@login_required
def add_invoice():
    if request.method == "GET":
        return render_template("add_invoice.html", products=get_products(), customers=get_customers())
    else:
        result = request.form
        items = np.column_stack([result.getlist('products_code[]'), result.getlist('qty[]')])
        invoice_id = insert_invoice(result['invoice_name'], result['customer'], items)
        return redirect(f"/invoice/{invoice_id}/")


""" Crud Invoice (D) """


@app.route("/invoice/delete/<invoice_id>/")
@login_required
def invoice_delete(invoice_id):
    remove_invoice(invoice_id)
    return redirect("/invoices/")
