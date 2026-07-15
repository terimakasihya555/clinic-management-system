from clinic_app.models import db
from clinic_app.models.medicine import Medicine
from clinic_app.utils.time import utc_now


class Prescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    visit_id = db.Column(db.Integer, db.ForeignKey("visit.id"), nullable=False)

    created_at = db.Column(db.DateTime, default=utc_now)

    items = db.relationship(
        "PrescriptionItem",
        backref="prescription",
        lazy=True
    )


class PrescriptionItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    prescription_id = db.Column(
        db.Integer,
        db.ForeignKey("prescription.id"),
        nullable=False
    )

    medicine_id = db.Column(
        db.Integer,
        db.ForeignKey("medicines.id"),
        nullable=False
    )

    qty = db.Column(db.Integer, nullable=False)

    medicine = db.relationship("Medicine")