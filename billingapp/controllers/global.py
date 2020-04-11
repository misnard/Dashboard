from billingapp import app
from flask import redirect, render_template
from flask_login import current_user


""" Handle unauthorized users """
@app.errorhandler(401)
def not_logged_in(e):
    return redirect("/login")


""" Handle page not found """
@app.errorhandler(404)
def not_logged_in(e):
    return render_template("404.html")


""" Inject user automatically if found """
@app.context_processor
def inject_user():
    return dict(user=current_user)
