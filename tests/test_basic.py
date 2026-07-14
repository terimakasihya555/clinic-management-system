import pytest

from clinic_app import create_app
from clinic_app.models import db


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
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


def test_login_page_loads(client):
    response = client.get("/auth/login")
    assert response.status_code == 200
    assert b"Login" in response.data or b"Masuk" in response.data


def test_dashboard_redirects_when_not_logged_in(client):
    response = client.get("/dashboard")
    assert response.status_code in [302, 401]


def test_404_page(client):
    response = client.get("/halaman-tidak-ada")
    assert response.status_code == 404


def test_queue_display_public_page(client):
    response = client.get("/queue/display")
    assert response.status_code == 200