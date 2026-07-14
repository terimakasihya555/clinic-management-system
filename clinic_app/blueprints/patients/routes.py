from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required

from clinic_app.models import db
from clinic_app.models.patient import Patient
from clinic_app.models.queue import QueueEntry
from clinic_app.models.visit import Visit
from clinic_app.models.user import User
from clinic_app.models.prescription import Prescription, PrescriptionItem
from clinic_app.models.medicine import Medicine
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


@patients_bp.route("/medical-record/<int:patient_id>")
@login_required
@role_required("admin", "doctor")
def medical_record(patient_id):
    patient = Patient.query.get_or_404(patient_id)

    visits = Visit.query.filter_by(
        patient_id=patient.id
    ).order_by(
        Visit.created_at.desc()
    ).all()

    visit_records = []

    for visit in visits:
        doctor = User.query.get(visit.doctor_id) if visit.doctor_id else None

        prescription = Prescription.query.filter_by(
            visit_id=visit.id
        ).first()

        prescription_items = []

        if prescription:
            items = PrescriptionItem.query.filter_by(
                prescription_id=prescription.id
            ).all()

            for item in items:
                medicine = Medicine.query.get(item.medicine_id)

                prescription_items.append({
                    "medicine": medicine,
                    "qty": item.qty
                })

        visit_records.append({
            "visit": visit,
            "doctor": doctor,
            "prescription_items": prescription_items
        })

    stats = {
        "total_visits": len(visit_records),
        "total_prescriptions": sum(
            1 for record in visit_records if record["prescription_items"]
        )
    }

    return render_template(
        "patients/medical_record.html",
        patient=patient,
        visit_records=visit_records,
        stats=stats
    )


@patients_bp.route("/delete/<int:patient_id>", methods=["POST"])
@login_required
@role_required("admin")
def delete(patient_id):
    patient = Patient.query.get_or_404(patient_id)

    related_queue = QueueEntry.query.filter_by(patient_id=patient.id).first()
    related_visit = Visit.query.filter_by(patient_id=patient.id).first()

    if related_queue or related_visit:
        flash(
            "Pasien tidak dapat dihapus karena sudah memiliki data antrian atau rekam medis.",
            "danger"
        )
        return redirect(url_for("patients.index"))

    db.session.delete(patient)
    db.session.commit()

    flash("Pasien berhasil dihapus.", "success")
    return redirect(url_for("patients.index"))