from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from clinic_app.models import db
from clinic_app.models.queue import QueueEntry
from clinic_app.models.visit import Visit
from clinic_app.models.medicine import Medicine
from clinic_app.security import role_required

doctor_bp = Blueprint("doctor", __name__, url_prefix="/doctor")

@doctor_bp.route("/")
@login_required
@role_required("admin", "doctor")
def dashboard():
    queue = QueueEntry.query.filter_by(status="waiting").order_by(QueueEntry.priority.asc(), QueueEntry.created_at.asc()).all()
    return render_template("doctor/dashboard.html", queue=queue)

@doctor_bp.route("/call/<int:queue_id>", methods=["POST"])
@login_required
@role_required("admin", "doctor")
def call(queue_id):
    entry = QueueEntry.query.get_or_404(queue_id)
    entry.status = "serving"
    db.session.commit()
    return redirect(url_for("doctor.visit", queue_id=entry.id))

@doctor_bp.route("/visit/<int:queue_id>", methods=["GET", "POST"])
@login_required
@role_required("admin", "doctor")
def visit(queue_id):
    entry = QueueEntry.query.get_or_404(queue_id)
    medicines = Medicine.query.order_by(Medicine.name).all()
    if request.method == "POST":
        visit = Visit(queue_id=entry.id, patient_id=entry.patient_id, doctor_id=current_user.id, diagnosis=request.form.get("diagnosis"), notes=request.form.get("notes"))
        entry.status = "done"
        db.session.add(visit)
        db.session.commit()
        flash("Pemeriksaan berhasil disimpan.", "success")
        return redirect(url_for("doctor.dashboard"))
    return render_template("doctor/visit_form.html", entry=entry, medicines=medicines)
