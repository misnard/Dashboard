from billingapp import app
from flask_login import login_required, current_user, login_user, logout_user
from flask import render_template, redirect, request, flash
from billingapp.helper import get_user

""" User login """
@app.route("/login/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        print(current_user.is_authenticated)
        if current_user is not None and current_user.is_authenticated is True:
            return redirect("/")
        return render_template("login.html")
    else:
        result = request.form
        user = get_user(result["email"])

        if not user or not user.key == user.hash_password(result["password"]):
            flash("Please check you login details and try again.")
            return redirect('/login/')

        login_user(user)
        return redirect("/")


""" User logout """
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login/')


""" User profile """
@app.route("/profile/")
@login_required
def profile():
    return render_template("profile.html")


""" User update infos """
@app.route("/profile/update_infos", methods=['POST'])
@login_required
def user_update_infos():
    result = request.form
    user = current_user

    user.update_user_infos(result["first_name"], result["last_name"])

    flash("You successfully update your infos.|success")

    return redirect('/profile/')


""" User update password """
@app.route("/profile/update_password", methods=['POST'])
@login_required
def user_update_password():
    result = request.form
    user = current_user

    if result["new_password"] != result["new_password_confirmation"]:
        flash("Your new password doesn't match with confirmation|danger")
    else:
        is_update_successfully = user.update_user_password(result["current_password"], result["new_password"])

        if is_update_successfully:
            flash("Your successfully update your password|success")
        else:
            flash("Your old password doesn't match|danger")

    return redirect('/profile')
