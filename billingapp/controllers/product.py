from billingapp import app
from flask import render_template, redirect, request
from flask_login import login_required
from billingapp.helper import insert_product, get_product, update_product, delete_product

""" Crud Product (C) """
@app.route("/product/add/", methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == "GET":
        return render_template('add_product.html')
    else:
        result = request.form
        insert_product(result['name'], result['code'], result['price_ht'])
        return redirect("/invoices")


""" Crud Product (U) """
@app.route("/product/edit/<product_id>/", methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    if request.method == "GET":
        return render_template('update_product.html', product=get_product(product_id))
    else:
        result = request.form
        update_product(product_id, result['name'], result['code'], result['price_ht'])
        return redirect(f"/product/edit/{product_id}")


""" Crud Product (D) """
@app.route("/product/delete/<product_id>/")
@login_required
def product_delete(product_id):
    delete_product(product_id)
    return redirect("/invoices/")