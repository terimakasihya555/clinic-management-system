from functools import wraps
from datetime import datetime, timedelta, timezone

from flask import request, abort, redirect, url_for, session, current_app
from flask_login import current_user, logout_user

from clinic_app.models import db
from clinic_app.models.audit_log import AuditLog


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


def get_utc_now():
    return datetime.now(timezone.utc)


def parse_session_datetime(value):
    if not value:
        return None

    try:
        parsed_value = datetime.fromisoformat(value)

        if parsed_value.tzinfo is None:
            parsed_value = parsed_value.replace(tzinfo=timezone.utc)

        return parsed_value

    except ValueError:
        return None


def get_client_ip():
    forwarded_for = request.headers.get("X-Forwarded-For")

    if forwarded_for:
        return forwarded_for.split(",")[0].strip()

    return request.remote_addr or "unknown"


def restrict_ip():
    if request.endpoint == "static":
        return None

    enable_ip_restriction = current_app.config.get(
        "ENABLE_IP_RESTRICTION",
        False
    )

    allowed_prefixes = current_app.config.get(
        "ALLOWED_IP_PREFIXES",
        ["127.", "192.168.", "10."]
    )

    if not enable_ip_restriction:
        return None

    client_ip = get_client_ip()

    if client_ip == "::1":
        return None

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
    now = get_utc_now()
    window_start = now - timedelta(seconds=window_seconds)

    if client_ip not in _rate_limit_storage:
        _rate_limit_storage[client_ip] = []

    _rate_limit_storage[client_ip] = [
        request_time
        for request_time in _rate_limit_storage[client_ip]
        if request_time >= window_start
    ]

    if len(_rate_limit_storage[client_ip]) >= max_requests:
        abort(429)

    _rate_limit_storage[client_ip].append(now)

    return None


def session_timeout():
    if request.endpoint == "static":
        return None

    if not current_user.is_authenticated:
        session.pop("last_activity", None)
        return None

    timeout_minutes = current_app.config.get("SESSION_TIMEOUT_MINUTES", 30)

    now = get_utc_now()
    last_activity = parse_session_datetime(session.get("last_activity"))

    if last_activity:
        inactive_time = now - last_activity

        if inactive_time > timedelta(minutes=timeout_minutes):
            logout_user()
            session.clear()
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
    if request.endpoint == "static":
        return response

    if request.method not in ["POST", "PUT", "PATCH", "DELETE"]:
        return response

    if response.status_code >= 500:
        return response

    try:
        user_id = current_user.id if current_user.is_authenticated else None

        audit_log = AuditLog(
            user_id=user_id,
            action=f"{request.method} {request.path}",
            module=request.blueprint or "general",
            record_id=None,
            details=f"Endpoint: {request.endpoint}",
            ip_address=get_client_ip(),
            user_agent=request.headers.get("User-Agent", "-")
        )

        db.session.add(audit_log)
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