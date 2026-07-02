from functools import wraps
from datetime import datetime, timedelta
from collections import defaultdict, deque
from flask import request, abort, current_app, redirect, url_for
from flask_login import current_user
from clinic_app.models import db
from clinic_app.models.audit_log import AuditLog

_rate_store = defaultdict(deque)

def init_security(app):
    app.before_request(restrict_ip)
    app.before_request(simple_rate_limit)
    app.after_request(set_security_headers)
    app.after_request(audit_after_request)

def restrict_ip():
    if not current_app.config.get("ENABLE_IP_RESTRICTION", False):
        return None
    client_ip = request.remote_addr or ""
    allowed = current_app.config.get("ALLOWED_IP_PREFIXES", ["127."])
    if not any(client_ip.startswith(prefix) for prefix in allowed):
        abort(403)

def simple_rate_limit():
    max_requests = current_app.config.get("RATE_LIMIT_MAX_REQUESTS", 200)
    window_seconds = current_app.config.get("RATE_LIMIT_WINDOW_SECONDS", 60)
    ip = request.remote_addr or "unknown"
    now = datetime.utcnow()
    q = _rate_store[ip]
    while q and q[0] < now - timedelta(seconds=window_seconds):
        q.popleft()
    if len(q) >= max_requests:
        abort(429)
    q.append(now)

def set_security_headers(response):
    response.headers.setdefault("X-Frame-Options", "DENY")
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("Referrer-Policy", "strict-origin-when-cross-origin")
    return response

def audit_after_request(response):
    try:
        if request.method in ["POST", "PUT", "PATCH", "DELETE"] and not request.path.startswith("/static"):
            log = AuditLog(
                user_id=current_user.id if current_user.is_authenticated else None,
                action=f"{request.method} {request.path}",
                module=request.path.split("/")[1] if len(request.path.split("/")) > 1 else "unknown",
                ip_address=request.remote_addr,
                user_agent=request.headers.get("User-Agent"),
            )
            db.session.add(log)
            db.session.commit()
    except Exception:
        db.session.rollback()
    return response

def role_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for("auth.login"))
            if current_user.role not in roles:
                abort(403)
            return func(*args, **kwargs)
        return wrapper
    return decorator
