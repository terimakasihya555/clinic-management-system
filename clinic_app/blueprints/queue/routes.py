from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, abort
from flask_login import login_required

from clinic_app.models import db
from clinic_app.models.patient import Patient
from clinic_app.models.queue import QueueEntry
from clinic_app.security import role_required
from clinic_app.utils.time import utc_now

queue_bp = Blueprint("queue", __name__, url_prefix="/queue")
def get_patient_or_404(patient_id):
    patient = db.session.get(Patient, patient_id)

    if not patient:
        abort(404)

    return patient

def get_queue_or_404(queue_id):
    queue_entry = db.session.get(QueueEntry, queue_id)

    if not queue_entry:
        abort(404)

    return queue_entry

@queue_bp.route("/")
@login_required
@role_required("admin", "receptionist", "doctor")
def index():
    status = request.args.get("status", "").strip()

    query = QueueEntry.query

    if status:
        query = query.filter_by(status=status)

    entries = query.order_by(
        QueueEntry.priority.asc(),
        QueueEntry.created_at.asc()
    ).all()

    total_waiting = QueueEntry.query.filter_by(status="waiting").count()
    total_serving = QueueEntry.query.filter_by(status="serving").count()
    total_done = QueueEntry.query.filter_by(status="done").count()

    stats = {
        "waiting": total_waiting,
        "serving": total_serving,
        "done": total_done,
    }

    return render_template(
        "queue/list.html",
        entries=entries,
        stats=stats,
        selected_status=status
    )


@queue_bp.route("/add/<int:patient_id>", methods=["POST"])
@login_required
@role_required("admin", "receptionist")
def add(patient_id):
    patient = get_patient_or_404(patient_id)

    kind = request.form.get("kind", "walkin")

    priority_map = {
        "emergency": 1,
        "appointment": 2,
        "walkin": 3
    }

    prefix_map = {
        "emergency": "E",
        "appointment": "A",
        "walkin": "W"
    }

    priority = priority_map.get(kind, 3)
    prefix = prefix_map.get(kind, "W")

    today = utc_now().date()

    count_today = QueueEntry.query.filter(
        db.func.date(QueueEntry.created_at) == today,
        QueueEntry.kind == kind
    ).count()

    number = f"{prefix}{count_today + 1:03d}"

    entry = QueueEntry(
        patient_id=patient_id,
        kind=kind,
        priority=priority,
        number=number,
        status="waiting"
    )

    db.session.add(entry)
    db.session.commit()

    flash(f"Nomor antrian {number} berhasil dibuat.", "success")
    return redirect(url_for("patients.index"))


@queue_bp.route("/finish/<int:queue_id>", methods=["POST"])
@login_required
@role_required("admin", "doctor")
def finish(queue_id):
    entry = get_queue_or_404(queue_id)
    entry.status = "done"
    db.session.commit()

    flash(f"Antrian {entry.number} telah diselesaikan.", "success")
    return redirect(url_for("queue.index"))


@queue_bp.route("/cancel/<int:queue_id>", methods=["POST"])
@login_required
@role_required("admin", "receptionist")
def cancel(queue_id):
    entry = get_queue_or_404(queue_id)

    db.session.delete(entry)
    db.session.commit()

    flash(f"Antrian {entry.number} berhasil dibatalkan.", "success")
    return redirect(url_for("queue.index"))

    flash(f"Antrian {entry.number} berhasil dibatalkan.", "success")
    return redirect(url_for("queue.index"))


@queue_bp.route("/display")
def display():
    entries = QueueEntry.query.filter_by(status="waiting").order_by(
        QueueEntry.priority.asc(),
        QueueEntry.created_at.asc()
    ).limit(5).all()

    serving = QueueEntry.query.filter_by(status="serving").order_by(
        QueueEntry.created_at.desc()
    ).first()

    return render_template(
        "queue/display.html",
        entries=entries,
        serving=serving
    )


@queue_bp.route("/api/top5")
def api_top5():
    entries = QueueEntry.query.filter_by(status="waiting").order_by(
        QueueEntry.priority.asc(),
        QueueEntry.created_at.asc()
    ).limit(5).all()

    return jsonify([
        {
            "number": entry.number,
            "patient": entry.patient.name,
            "kind": entry.kind,
            "status": entry.status
        }
        for entry in entries
    ])