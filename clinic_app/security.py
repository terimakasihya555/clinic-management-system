from datetime import datetime, timedelta
from functools import wraps

from flask import request, abort, current_app, session, flash, redirect, url_for
from flask_login import current_user, logout_user

from clinic_app.models import db


_rate_limit_storage = {}


def role_required(*allowed_roles):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for("auth.login"))

            if current_user.role not in allowed_roles:
                abort(403)

            return function(*args, **kwargs)

        return wrapper

    return decorator


def get_client_ip():
    forwarded_for = request.headers.get("X-Forwarded-For")

    if forwarded_for:
        return forwarded_for.split(",")[0].strip()

    return request.remote_addr or "unknown"


def restrict_ip():
    if request.endpoint == "static":
        return None

    if not current_app.config.get("ENABLE_IP_RESTRICTION", False):
        return None

    client_ip = get_client_ip()
    allowed_prefixes = current_app.config.get("ALLOWED_IP_PREFIXES", [])

    is_allowed = any(
        client_ip.startswith(prefix)
        for prefix in allowed_prefixes
    )

    if not is_allowed:
        abort(403)

    return None


def simple_rate_limit():
    if request.endpoint == "static":
        return None

    max_requests = current_app.config.get("RATE_LIMIT_MAX_REQUESTS", 200)
    window_seconds = current_app.config.get("RATE_LIMIT_WINDOW_SECONDS", 60)

    client_ip = get_client_ip()
    now = datetime.utcnow()
    window_start = now - timedelta(seconds=window_seconds)

    request_times = _rate_limit_storage.get(client_ip, [])

    request_times = [
        request_time
        for request_time in request_times
        if request_time > window_start
    ]

    if len(request_times) >= max_requests:
        abort(429)

    request_times.append(now)
    _rate_limit_storage[client_ip] = request_times

    return None


def session_timeout():
    if request.endpoint == "static":
        return None

    if not current_user.is_authenticated:
        return None

    timeout_minutes = current_app.config.get("SESSION_TIMEOUT_MINUTES", 30)
    now = datetime.utcnow()

    last_activity = session.get("last_activity")

    if last_activity:
        last_activity_time = datetime.fromisoformat(last_activity)
        timeout_limit = timedelta(minutes=timeout_minutes)

        if now - last_activity_time > timeout_limit:
            logout_user()
            session.clear()
            flash("Sesi login telah berakhir. Silakan login kembali.", "warning")
            return redirect(url_for("auth.login"))

    session["last_activity"] = now.isoformat()

    return None


def set_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"

    return response


def audit_after_request(response):
    try:
        if request.endpoint == "static":
            return response

        if request.method not in ["POST", "PUT", "PATCH", "DELETE"]:
            return response

        from clinic_app.models.audit_log import AuditLog

        endpoint = request.endpoint or "-"
        module = endpoint.split(".")[0] if "." in endpoint else endpoint
        client_ip = get_client_ip()
        user_agent = request.headers.get("User-Agent", "-")

        user_id = None

        if current_user and current_user.is_authenticated:
            user_id = current_user.id

        log = AuditLog(
            user_id=user_id,
            action=f"{request.method} {request.path}",
            module=module,
            record_id=None,
            details=f"Status code: {response.status_code}",
            ip_address=client_ip,
            user_agent=user_agent
        )

        db.session.add(log)
        db.session.commit()

    except Exception:
        db.session.rollback()

    return response


def init_security(app):
    app.before_request(restrict_ip)
    app.before_request(simple_rate_limit)
    app.before_request(session_timeout)

    app.after_request(set_security_headers)
    app.after_request(audit_after_request)