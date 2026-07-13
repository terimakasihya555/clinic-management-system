from flask import Blueprint, render_template, request
from flask_login import login_required

from clinic_app.models.audit_log import AuditLog
from clinic_app.models.user import User
from clinic_app.security import role_required

audit_bp = Blueprint("audit", __name__, url_prefix="/audit")


@audit_bp.route("/")
@login_required
@role_required("admin")
def index():
    keyword = request.args.get("q", "").strip()
    module = request.args.get("module", "").strip()
    user_id = request.args.get("user_id", "").strip()

    query = AuditLog.query

    if keyword:
        query = query.filter(
            AuditLog.action.ilike(f"%{keyword}%")
        )

    if module:
        query = query.filter_by(module=module)

    if user_id:
        query = query.filter_by(user_id=int(user_id))

    logs = query.order_by(
        AuditLog.timestamp.desc()
    ).limit(300).all()

    users = User.query.order_by(User.name.asc()).all()

    modules = [
        row[0]
        for row in AuditLog.query.with_entities(AuditLog.module)
        .distinct()
        .all()
        if row[0]
    ]

    total_logs = AuditLog.query.count()
    auth_logs = AuditLog.query.filter_by(module="auth").count()
    patient_logs = AuditLog.query.filter_by(module="patients").count()
    queue_logs = AuditLog.query.filter_by(module="queue").count()

    stats = {
        "total_logs": total_logs,
        "auth_logs": auth_logs,
        "patient_logs": patient_logs,
        "queue_logs": queue_logs,
    }

    return render_template(
        "audit/list.html",
        logs=logs,
        users=users,
        modules=modules,
        stats=stats,
        keyword=keyword,
        selected_module=module,
        selected_user_id=user_id
    )