from flask import Blueprint, render_template
from flask_login import login_required
from clinic_app.models.audit_log import AuditLog
from clinic_app.security import role_required

audit_bp = Blueprint("audit", __name__, url_prefix="/audit")

@audit_bp.route("/")
@login_required
@role_required("admin")
def index():
    logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).limit(200).all()
    return render_template("audit/list.html", logs=logs)
