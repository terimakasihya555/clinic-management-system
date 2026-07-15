import pytest
from werkzeug.security import generate_password_hash

from clinic_app import create_app
from clinic_app.models import db
from clinic_app.models.user import User
from clinic_app.models.patient import Patient
from clinic_app.models.medicine import Medicine
from clinic_app.models.audit_log import AuditLog


@pytest.fixture
def app(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///:memory:")
    monkeypatch.setenv("SECRET_KEY", "test-secret-key")

    app = create_app()

    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SECRET_KEY="test-secret-key"
    )

    with app.app_context():
        db.drop_all()
        db.create_all()

        admin = User(
            name="Admin Test",
            email="admin@test.local",
            password_hash=generate_password_hash("admin123"),
            role="admin"
        )

        doctor = User(
            name="Doctor Test",
            email="doctor@test.local",
            password_hash=generate_password_hash("doctor123"),
            role="doctor"
        )

        receptionist = User(
            name="Receptionist Test",
            email="reception@test.local",
            password_hash=generate_password_hash("reception123"),
            role="receptionist"
        )

        patient = Patient(
            medical_record_number="RM00001",
            name="Budi Test",
            birthdate="2000-01-01",
            gender="Laki-laki",
            phone="08123456789",
            address="Jakarta"
        )

        medicine = Medicine(
            name="Paracetamol Test",
            unit="tablet",
            category="Analgesik",
            description="Obat demam",
            stock=50
        )

        db.session.add_all([
            admin,
            doctor,
            receptionist,
            patient,
            medicine
        ])
        db.session.commit()

        audit_log = AuditLog(
            user_id=admin.id,
            action="TEST_ACTION",
            module="test",
            record_id="1",
            details="Testing audit export",
            ip_address="127.0.0.1",
            user_agent="pytest"
        )

        db.session.add(audit_log)
        db.session.commit()

    yield app

    with app.app_context():
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


def logout(client):
    return client.get("/auth/logout", follow_redirects=True)


def assert_excel_response(response):
    assert response.status_code == 200
    assert "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" in response.content_type
    assert response.data[:2] == b"PK"


def test_admin_can_update_patient(client, app):
    login(client, "admin@test.local", "admin123")

    with app.app_context():
        patient = Patient.query.first()
        patient_id = patient.id

    response = client.post(
        f"/patients/update/{patient_id}",
        data={
            "name": "Budi Updated",
            "birthdate": "2001-02-02",
            "gender": "Laki-laki",
            "phone": "08999999999",
            "address": "Bandung"
        },
        follow_redirects=True
    )

    assert response.status_code == 200

    with app.app_context():
        updated_patient = Patient.query.get(patient_id)
        assert updated_patient.name == "Budi Updated"
        assert updated_patient.phone == "08999999999"
        assert updated_patient.address == "Bandung"


def test_doctor_cannot_update_patient(client, app):
    login(client, "doctor@test.local", "doctor123")

    with app.app_context():
        patient = Patient.query.first()
        patient_id = patient.id

    response = client.post(
        f"/patients/update/{patient_id}",
        data={
            "name": "Unauthorized Update",
            "birthdate": "2001-02-02",
            "gender": "Laki-laki",
            "phone": "08000000000",
            "address": "Unauthorized"
        },
        follow_redirects=False
    )

    assert response.status_code == 403


def test_export_patients_excel(client):
    login(client, "admin@test.local", "admin123")

    response = client.get("/patients/export")

    assert_excel_response(response)


def test_export_medical_record_excel(client, app):
    login(client, "admin@test.local", "admin123")

    with app.app_context():
        patient = Patient.query.first()
        patient_id = patient.id

    response = client.get(f"/patients/medical-record/{patient_id}/export")

    assert_excel_response(response)


def test_export_inventory_excel(client):
    login(client, "admin@test.local", "admin123")

    response = client.get("/inventory/export")

    assert_excel_response(response)


def test_export_audit_log_excel(client):
    login(client, "admin@test.local", "admin123")

    response = client.get("/audit/export")

    assert_excel_response(response)