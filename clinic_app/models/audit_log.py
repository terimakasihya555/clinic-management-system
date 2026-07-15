from clinic_app.models import db
from clinic_app.utils.time import utc_now


class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)

    action = db.Column(db.String(100), nullable=False)
    module = db.Column(db.String(100), nullable=True)
    record_id = db.Column(db.String(100), nullable=True)
    details = db.Column(db.Text, nullable=True)

    ip_address = db.Column(db.String(100), nullable=True)
    user_agent = db.Column(db.Text, nullable=True)

    timestamp = db.Column(db.DateTime, default=utc_now)

    user = db.relationship("User", backref="audit_logs")