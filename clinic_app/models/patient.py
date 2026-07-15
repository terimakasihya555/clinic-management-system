from clinic_app.models import db
from clinic_app.utils.time import utc_now


class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    medical_record_number = db.Column(db.String(50), unique=True, nullable=True)

    name = db.Column(db.String(150), nullable=False)
    birthdate = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(20), nullable=True)
    phone = db.Column(db.String(50), nullable=True)
    address = db.Column(db.Text, nullable=True)

    created_at = db.Column(db.DateTime, default=utc_now)