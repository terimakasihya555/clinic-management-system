from datetime import datetime
from clinic_app.models import db

class QueueEntry(db.Model):
    __tablename__ = "queue_entries"
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey("patients.id"), nullable=False)
    kind = db.Column(db.String(20), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default="waiting")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    patient = db.relationship("Patient", backref="queue_entries")
