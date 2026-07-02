from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash
from clinic_app.models.user import User

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    if request.method == "POST":
        user = User.query.filter_by(email=request.form.get("email","").lower().strip()).first()
        if user and check_password_hash(user.password_hash, request.form.get("password","")):
            login_user(user)
            flash("Login berhasil.", "success")
            return redirect(url_for("index"))
        flash("Email atau password salah.", "danger")
    return render_template("auth/login.html")

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout berhasil.", "success")
    return redirect(url_for("auth.login"))
