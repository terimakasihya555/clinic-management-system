from flask_login import UserMixin

from clinic_app.models import db
from clinic_app.utils.time import utc_now


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(50), nullable=False)

    created_at = db.Column(db.DateTime, default=utc_now)