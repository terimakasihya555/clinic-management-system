from clinic_app import create_app
from clinic_app.models import db, load_models


def test_health_check_returns_ok(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    monkeypatch.setenv("SECRET_KEY", "test-secret-key")

    app = create_app()

    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SECRET_KEY="test-secret-key"
    )

    with app.app_context():
        load_models()
        db.drop_all()
        db.create_all()

    client = app.test_client()

    response = client.get("/health/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "ok"
    assert data["app"] == "Clinic Management System"
    assert data["version"] == "1.0.0"
    assert data["database"] == "connected"