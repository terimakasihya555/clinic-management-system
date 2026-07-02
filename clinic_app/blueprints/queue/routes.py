from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from clinic_app.models import db
from clinic_app.models.patient import Patient
from clinic_app.models.queue import QueueEntry
from clinic_app.security import role_required

queue_bp = Blueprint("queue", __name__, url_prefix="/queue")

@queue_bp.route("/")
@login_required
@role_required("admin", "receptionist", "doctor")
def index():
    entries = QueueEntry.query.order_by(QueueEntry.priority.asc(), QueueEntry.created_at.asc()).all()
    return render_template("queue/list.html", entries=entries)

@queue_bp.route("/add/<int:patient_id>", methods=["POST"])
@login_required
@role_required("admin", "receptionist")
def add(patient_id):
    Patient.query.get_or_404(patient_id)
    kind = request.form.get("kind", "walkin")
    priority_map = {"emergency": 1, "appointment": 2, "walkin": 3}
    prefix_map = {"emergency": "E", "appointment": "A", "walkin": "W"}
    count = QueueEntry.query.filter(db.func.date(QueueEntry.created_at) == datetime.utcnow().date(), QueueEntry.kind == kind).count()
    entry = QueueEntry(patient_id=patient_id, kind=kind, priority=priority_map.get(kind,3), number=f"{prefix_map.get(kind,'W')}{count+1:03d}")
    db.session.add(entry)
    db.session.commit()
    flash(f"Nomor antrian {entry.number} berhasil dibuat.", "success")
    return redirect(url_for("patients.index"))

@queue_bp.route("/display")
def display():
    entries = QueueEntry.query.filter_by(status="waiting").order_by(QueueEntry.priority.asc(), QueueEntry.created_at.asc()).limit(5).all()
    return render_template("queue/display.html", entries=entries)

@queue_bp.route("/api/top5")
def api_top5():
    entries = QueueEntry.query.filter_by(status="waiting").order_by(QueueEntry.priority.asc(), QueueEntry.created_at.asc()).limit(5).all()
    return jsonify([{"number": e.number, "patient": e.patient.name, "status": e.status} for e in entries])
