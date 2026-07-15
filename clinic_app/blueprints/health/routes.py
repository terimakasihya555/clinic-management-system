from flask import Blueprint, jsonify
from sqlalchemy import text

from clinic_app.models import db


health_bp = Blueprint("health", __name__, url_prefix="/health")


@health_bp.route("/")
def health_check():
    try:
        db.session.execute(text("SELECT 1"))

        database_status = "connected"
        status_code = 200

    except Exception:
        database_status = "error"
        status_code = 500

    return jsonify({
        "status": "ok" if status_code == 200 else "error",
        "app": "Clinic Management System",
        "database": database_status
    }), status_code