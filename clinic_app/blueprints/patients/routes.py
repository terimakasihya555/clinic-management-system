from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from clinic_app.models import db
from clinic_app.models.patient import Patient
from clinic_app.security import role_required

patients_bp = Blueprint("patients", __name__, url_prefix="/patients")

@patients_bp.route("/")
@login_required
@role_required("admin", "receptionist", "doctor")
def index():
    patients = Patient.query.order_by(Patient.created_at.desc()).all()
    return render_template("patients/list.html", patients=patients)

@patients_bp.route("/create", methods=["POST"])
@login_required
@role_required("admin", "receptionist")
def create():
    p = Patient(
        name=request.form.get("name"),
        birthdate=request.form.get("birthdate"),
        gender=request.form.get("gender"),
        phone=request.form.get("phone"),
        address=request.form.get("address"),
    )
    db.session.add(p)
    db.session.commit()
    p.medical_record_number = f"RM{p.id:05d}"
    db.session.commit()
    flash("Pasien berhasil ditambahkan.", "success")
    return redirect(url_for("patients.index"))
