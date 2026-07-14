import pytest
from werkzeug.security import generate_password_hash

from clinic_app import create_app
from clinic_app.models import db
from clinic_app.models.user import User


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        WTF_CSRF_ENABLED=False,
        ENABLE_IP_RESTRICTION=False,
    )

    with app.app_context():
        db.create_all()

        admin = User(
            name="Admin Test",
            email="admin@test.com",
            role="admin",
            password_hash=generate_password_hash("admin123")
        )

        doctor = User(
            name="Doctor Test",
            email="doctor@test.com",
            role="doctor",
            password_hash=generate_password_hash("doctor123")
        )

        db.session.add(admin)
        db.session.add(doctor)
        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def login(client, email, password):
    return client.post(
        "/auth/login",
        data={
            "email": email,
            "password": password
        },
        follow_redirects=True
    )


def test_admin_login_success(client):
    response = login(client, "admin@test.com", "admin123")
    assert response.status_code == 200
    assert b"Dashboard" in response.data or b"dashboard" in response.data


def test_invalid_login_failed(client):
    response = login(client, "admin@test.com", "salahpassword")
    assert response.status_code == 200
    assert b"Login" in response.data or b"Invalid" in response.data or b"salah" in response.data


def test_doctor_cannot_access_users_page(client):
    login(client, "doctor@test.com", "doctor123")
    response = client.get("/users/")
    assert response.status_code == 403


def test_admin_can_access_users_page(client):
    login(client, "admin@test.com", "admin123")
    response = client.get("/users/")
    assert response.status_code == 200