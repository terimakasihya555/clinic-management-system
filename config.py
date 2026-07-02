class Config:
    SECRET_KEY = "change-this-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///clinic.sqlite"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENABLE_IP_RESTRICTION = False
    ALLOWED_IP_PREFIXES = ["127.", "192.168.1.", "10.0.0."]
    RATE_LIMIT_MAX_REQUESTS = 200
    RATE_LIMIT_WINDOW_SECONDS = 60
