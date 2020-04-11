from billingapp import app
from flask import render_template, redirect, request
from flask_login import login_required
from billingapp.helper import insert_customer, get_customer, update_customer, delete_customer

""" Crud Customer (C) """
@app.route("/customer/add/", methods=['GET', 'POST'])
@login_required
def add_customer():
    if request.method == "GET":
        return render_template('add_customer.html')
    else:
        result = request.form
        insert_customer(result['name'], result['siret'], result['email'], result['phone'], result['address'])
        return redirect("/invoices")


""" Crud Customer (U) """
@app.route("/customer/edit/<customer_id>/", methods=['GET', 'POST'])
@login_required
def edit_customer(customer_id):
    if request.method == "GET":
        return render_template('update_customer.html', customer=get_customer(customer_id))
    else:
        result = request.form
        update_customer(customer_id, result['name'], result['siret'], result['email'], result['phone'],
                        result['address'])
        return redirect(f"/customer/edit/{customer_id}")


""" Crud Customer (D) """
@app.route("/customer/delete/<customer_id>/")
@login_required
def customer_delete(customer_id):
    delete_customer(customer_id)
    return redirect("/invoices/")