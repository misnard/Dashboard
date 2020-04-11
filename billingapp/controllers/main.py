from billingapp import app
from flask_login import login_required
from flask import render_template
from billingapp.helper import get_pending_invoices


@app.route('/')
@login_required
def index():
    return render_template("index.html", invoice_count=len(get_pending_invoices()))