from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from clinic_app.models import db
from clinic_app.models.queue import QueueEntry
from clinic_app.models.visit import Visit
from clinic_app.models.medicine import Medicine
from clinic_app.models.prescription import Prescription, PrescriptionItem
from clinic_app.security import role_required

doctor_bp = Blueprint("doctor", __name__, url_prefix="/doctor")


@doctor_bp.route("/")
@login_required
@role_required("admin", "doctor")
def dashboard():
    queue = QueueEntry.query.filter_by(status="waiting").order_by(
        QueueEntry.priority.asc(),
        QueueEntry.created_at.asc()
    ).all()

    return render_template("doctor/dashboard.html", queue=queue)


@doctor_bp.route("/call/<int:queue_id>", methods=["POST"])
@login_required
@role_required("admin", "doctor")
def call(queue_id):
    entry = QueueEntry.query.get_or_404(queue_id)

    entry.status = "serving"
    db.session.commit()

    flash(f"Pasien {entry.patient.name} sedang dipanggil.", "success")
    return redirect(url_for("doctor.visit", queue_id=entry.id))


@doctor_bp.route("/visit/<int:queue_id>", methods=["GET", "POST"])
@login_required
@role_required("admin", "doctor")
def visit(queue_id):
    entry = QueueEntry.query.get_or_404(queue_id)
    medicines = Medicine.query.order_by(Medicine.name.asc()).all()

    if request.method == "POST":
        diagnosis = request.form.get("diagnosis", "").strip()
        notes = request.form.get("notes", "").strip()

        if not diagnosis:
            flash("Diagnosis wajib diisi.", "danger")
            return redirect(url_for("doctor.visit", queue_id=entry.id))

        selected_items = []

        for medicine in medicines:
            qty_raw = request.form.get(f"medicine_{medicine.id}", "0").strip()

            if qty_raw == "":
                qty = 0
            else:
                try:
                    qty = int(qty_raw)
                except ValueError:
                    flash(f"Jumlah obat {medicine.name} tidak valid.", "danger")
                    return redirect(url_for("doctor.visit", queue_id=entry.id))

            if qty < 0:
                flash(f"Jumlah obat {medicine.name} tidak boleh negatif.", "danger")
                return redirect(url_for("doctor.visit", queue_id=entry.id))

            if qty > 0:
                if medicine.stock < qty:
                    flash(
                        f"Stok {medicine.name} tidak cukup. "
                        f"Stok tersedia: {medicine.stock} {medicine.unit}.",
                        "danger"
                    )
                    return redirect(url_for("doctor.visit", queue_id=entry.id))

                selected_items.append({
                    "medicine": medicine,
                    "qty": qty
                })

        visit_record = Visit(
            queue_id=entry.id,
            patient_id=entry.patient_id,
            doctor_id=current_user.id,
            diagnosis=diagnosis,
            notes=notes
        )

        db.session.add(visit_record)
        db.session.flush()

        prescription = Prescription(
            visit_id=visit_record.id
        )

        db.session.add(prescription)
        db.session.flush()

        for item in selected_items:
            medicine = item["medicine"]
            qty = item["qty"]

            prescription_item = PrescriptionItem(
                prescription_id=prescription.id,
                medicine_id=medicine.id,
                qty=qty
            )

            medicine.stock -= qty
            db.session.add(prescription_item)

        entry.status = "done"

        db.session.commit()

        flash("Pemeriksaan dan resep berhasil disimpan.", "success")
        return redirect(url_for("doctor.dashboard"))

    return render_template(
        "doctor/visit_form.html",
        entry=entry,
        medicines=medicines
    )