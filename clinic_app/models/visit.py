from clinic_app.models import db
from clinic_app.utils.time import utc_now


class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    queue_id = db.Column(db.Integer, db.ForeignKey("queue_entry.id"), nullable=False)
    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    diagnosis = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=utc_now)

    queue = db.relationship("QueueEntry")
    patient = db.relationship("Patient")
    doctor = db.relationship("User")