import os
from dotenv import load_dotenv

load_dotenv()


def str_to_bool(value, default=False):
    if value is None:
        return default

    return str(value).strip().lower() in ["true", "1", "yes", "y", "on"]


def str_to_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def str_to_list(value, default):
    if not value:
        return default

    return [
        item.strip()
        for item in value.split(",")
        if item.strip()
    ]


class Config:
    APP_NAME = "Clinic Management System"
    APP_VERSION = os.environ.get("APP_VERSION", "1.0.0")

    SECRET_KEY = os.environ.get("SECRET_KEY", "change-this-secret-key")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "sqlite:///clinic.sqlite"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ENABLE_IP_RESTRICTION = str_to_bool(
        os.environ.get("ENABLE_IP_RESTRICTION"),
        False
    )

    ALLOWED_IP_PREFIXES = str_to_list(
        os.environ.get("ALLOWED_IP_PREFIXES"),
        ["127.", "192.168.", "10."]
    )

    RATE_LIMIT_MAX_REQUESTS = str_to_int(
        os.environ.get("RATE_LIMIT_MAX_REQUESTS"),
        200
    )

    RATE_LIMIT_WINDOW_SECONDS = str_to_int(
        os.environ.get("RATE_LIMIT_WINDOW_SECONDS"),
        60
    )

    SESSION_TIMEOUT_MINUTES = str_to_int(
        os.environ.get("SESSION_TIMEOUT_MINUTES"),
        30
    )

    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    SESSION_COOKIE_SECURE = str_to_bool(
        os.environ.get("SESSION_COOKIE_SECURE"),
        False
    )