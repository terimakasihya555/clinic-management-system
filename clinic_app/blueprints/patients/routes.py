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
    keyword = request.args.get("q", "").strip()

    if keyword:
        patients = Patient.query.filter(
            Patient.name.ilike(f"%{keyword}%")
        ).order_by(Patient.created_at.desc()).all()
    else:
        patients = Patient.query.order_by(
            Patient.created_at.desc()
        ).all()

    return render_template(
        "patients/list.html",
        patients=patients,
        keyword=keyword
    )


@patients_bp.route("/create", methods=["POST"])
@login_required
@role_required("admin", "receptionist")
def create():
    name = request.form.get("name", "").strip()
    birthdate = request.form.get("birthdate")
    gender = request.form.get("gender")
    phone = request.form.get("phone")
    address = request.form.get("address")

    if not name:
        flash("Nama pasien wajib diisi.", "danger")
        return redirect(url_for("patients.index"))

    patient = Patient(
        name=name,
        birthdate=birthdate,
        gender=gender,
        phone=phone,
        address=address,
    )

    db.session.add(patient)
    db.session.commit()

    patient.medical_record_number = f"RM{patient.id:05d}"
    db.session.commit()

    flash("Pasien berhasil ditambahkan.", "success")
    return redirect(url_for("patients.index"))


@patients_bp.route("/delete/<int:patient_id>", methods=["POST"])
@login_required
@role_required("admin")
def delete(patient_id):
    patient = Patient.query.get_or_404(patient_id)

    db.session.delete(patient)
    db.session.commit()

    flash("Pasien berhasil dihapus.", "success")
    return redirect(url_for("patients.index"))