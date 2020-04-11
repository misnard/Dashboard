from billingapp import app
from flask import redirect, request
from flask_login import login_required
from billingapp.helper import update_enterprise

""" Crud Product (U) """


@app.route("/enterprise/edit", methods=['POST'])
@login_required
def edit_enterprise():
    result = request.form

    update_enterprise(result['name'], result['address'], result['city'], result['phone'], result['email'],
                      result['postal-code'], result['siret'], result['bank'])
    return redirect("/invoices")
