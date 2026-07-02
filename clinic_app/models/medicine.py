from clinic_app.models import db

class Medicine(db.Model):
    __tablename__ = "medicines"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    unit = db.Column(db.String(30), nullable=False)
    category = db.Column(db.String(120))
    description = db.Column(db.Text)
    stock = db.Column(db.Integer, default=0)
