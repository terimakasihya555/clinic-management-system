import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret-key")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///clinic.sqlite"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security configuration
    ENABLE_IP_RESTRICTION = False

    # Untuk local development:
    # 127. = localhost
    # 192.168. = jaringan WiFi/LAN umum
    # 10. = jaringan privat
    ALLOWED_IP_PREFIXES = [
        "127.",
        "192.168.",
        "10."
    ]

    RATE_LIMIT_MAX_REQUESTS = 200
    RATE_LIMIT_WINDOW_SECONDS = 60

    SESSION_TIMEOUT_MINUTES = 30

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"

    # Saat deploy pakai HTTPS, ubah menjadi True
    SESSION_COOKIE_SECURE = False