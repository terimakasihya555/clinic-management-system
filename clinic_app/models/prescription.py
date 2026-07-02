from datetime import datetime
from clinic_app.models import db

class Prescription(db.Model):
    __tablename__ = "prescriptions"
    id = db.Column(db.Integer, primary_key=True)
    visit_id = db.Column(db.Integer, db.ForeignKey("visits.id"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    visit = db.relationship("Visit", backref="prescriptions")

class PrescriptionItem(db.Model):
    __tablename__ = "prescription_items"
    id = db.Column(db.Integer, primary_key=True)
    prescription_id = db.Column(db.Integer, db.ForeignKey("prescriptions.id"), nullable=False)
    medicine_id = db.Column(db.Integer, db.ForeignKey("medicines.id"), nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    prescription = db.relationship("Prescription", backref="items")
    medicine = db.relationship("Medicine")
