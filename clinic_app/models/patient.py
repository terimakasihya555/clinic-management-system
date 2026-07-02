from datetime import datetime
from clinic_app.models import db

class Patient(db.Model):
    __tablename__ = "patients"
    id = db.Column(db.Integer, primary_key=True)
    medical_record_number = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(120), nullable=False)
    birthdate = db.Column(db.String(20))
    gender = db.Column(db.String(20))
    phone = db.Column(db.String(30))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
