from clinic_app.models import db
from clinic_app.utils.time import utc_now


class QueueEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    patient_id = db.Column(db.Integer, db.ForeignKey("patient.id"), nullable=False)

    kind = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    priority = db.Column(db.Integer, nullable=False)

    status = db.Column(db.String(50), default="waiting")

    created_at = db.Column(db.DateTime, default=utc_now)

    patient = db.relationship("Patient", backref="queues")