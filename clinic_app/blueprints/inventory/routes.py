from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from clinic_app.models import db
from clinic_app.models.medicine import Medicine
from clinic_app.security import role_required

inventory_bp = Blueprint("inventory", __name__, url_prefix="/inventory")

@inventory_bp.route("/")
@login_required
@role_required("admin", "receptionist")
def index():
    medicines = Medicine.query.order_by(Medicine.name).all()
    return render_template("inventory/list.html", medicines=medicines)

@inventory_bp.route("/create", methods=["POST"])
@login_required
@role_required("admin")
def create():
    med = Medicine(name=request.form.get("name"), unit=request.form.get("unit"), category=request.form.get("category"), description=request.form.get("description"), stock=int(request.form.get("stock", 0)))
    db.session.add(med)
    db.session.commit()
    flash("Obat berhasil ditambahkan.", "success")
    return redirect(url_for("inventory.index"))
