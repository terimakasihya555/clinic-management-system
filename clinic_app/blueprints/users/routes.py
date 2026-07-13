from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash

from clinic_app.models import db
from clinic_app.models.user import User
from clinic_app.security import role_required


users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/")
@login_required
@role_required("admin")
def index():
    keyword = request.args.get("q", "").strip()
    role = request.args.get("role", "").strip()

    query = User.query

    if keyword:
        query = query.filter(User.name.ilike(f"%{keyword}%"))

    if role:
        query = query.filter_by(role=role)

    users = query.order_by(User.created_at.desc()).all()

    stats = {
        "total_users": User.query.count(),
        "total_admin": User.query.filter_by(role="admin").count(),
        "total_doctor": User.query.filter_by(role="doctor").count(),
        "total_receptionist": User.query.filter_by(role="receptionist").count(),
    }

    return render_template(
        "users/list.html",
        users=users,
        stats=stats,
        keyword=keyword,
        selected_role=role
    )


@users_bp.route("/create", methods=["POST"])
@login_required
@role_required("admin")
def create():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").lower().strip()
    password = request.form.get("password", "").strip()
    role = request.form.get("role", "").strip()

    if not name:
        flash("Nama user wajib diisi.", "danger")
        return redirect(url_for("users.index"))

    if not email:
        flash("Email user wajib diisi.", "danger")
        return redirect(url_for("users.index"))

    if not password:
        flash("Password user wajib diisi.", "danger")
        return redirect(url_for("users.index"))

    if role not in ["admin", "doctor", "receptionist"]:
        flash("Role user tidak valid.", "danger")
        return redirect(url_for("users.index"))

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        flash("Email sudah digunakan oleh user lain.", "danger")
        return redirect(url_for("users.index"))

    user = User(
        name=name,
        email=email,
        role=role,
        password_hash=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()

    flash("User baru berhasil ditambahkan.", "success")
    return redirect(url_for("users.index"))


@users_bp.route("/update/<int:user_id>", methods=["POST"])
@login_required
@role_required("admin")
def update(user_id):
    user = User.query.get_or_404(user_id)

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").lower().strip()
    role = request.form.get("role", "").strip()
    password = request.form.get("password", "").strip()

    if not name:
        flash("Nama user wajib diisi.", "danger")
        return redirect(url_for("users.index"))

    if not email:
        flash("Email user wajib diisi.", "danger")
        return redirect(url_for("users.index"))

    duplicate = User.query.filter(
        User.email == email,
        User.id != user.id
    ).first()

    if duplicate:
        flash("Email sudah digunakan oleh user lain.", "danger")
        return redirect(url_for("users.index"))

    user.name = name
    user.email = email

    # Akun yang sedang login tidak boleh mengubah role sendiri.
    # Ini mencegah admin kehilangan akses ke halaman User Management.
    if user.id == current_user.id:
        user.role = current_user.role
    else:
        if role not in ["admin", "doctor", "receptionist"]:
            flash("Role user tidak valid.", "danger")
            return redirect(url_for("users.index"))

        user.role = role

    if password:
        user.password_hash = generate_password_hash(password)

    db.session.commit()

    flash("Data user berhasil diperbarui.", "success")
    return redirect(url_for("users.index"))


@users_bp.route("/delete/<int:user_id>", methods=["POST"])
@login_required
@role_required("admin")
def delete(user_id):
    user = User.query.get_or_404(user_id)

    if user.id == current_user.id:
        flash("Kamu tidak bisa menghapus akun yang sedang digunakan.", "danger")
        return redirect(url_for("users.index"))

    db.session.delete(user)
    db.session.commit()

    flash("User berhasil dihapus.", "success")
    return redirect(url_for("users.index"))