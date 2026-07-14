from werkzeug.security import generate_password_hash

from clinic_app import create_app
from clinic_app.models import db
from clinic_app.models.user import User
from clinic_app.models.patient import Patient
from clinic_app.models.queue import QueueEntry
from clinic_app.models.medicine import Medicine
from clinic_app.models.visit import Visit
from clinic_app.models.prescription import Prescription, PrescriptionItem
from clinic_app.models.audit_log import AuditLog


app = create_app()


def get_or_create_user(name, email, role, password):
    user = User.query.filter_by(email=email).first()

    if user:
        return user

    user = User(
        name=name,
        email=email,
        role=role,
        password_hash=generate_password_hash(password)
    )

    db.session.add(user)
    db.session.commit()

    return user


def get_or_create_medicine(name, unit, category, description, stock):
    medicine = Medicine.query.filter_by(name=name).first()

    if medicine:
        return medicine

    medicine = Medicine(
        name=name,
        unit=unit,
        category=category,
        description=description,
        stock=stock
    )

    db.session.add(medicine)
    db.session.commit()

    return medicine


def get_or_create_patient(name, birthdate, gender, phone, address):
    patient = Patient.query.filter_by(name=name, phone=phone).first()

    if patient:
        return patient

    patient = Patient(
        name=name,
        birthdate=birthdate,
        gender=gender,
        phone=phone,
        address=address
    )

    db.session.add(patient)
    db.session.commit()

    patient.medical_record_number = f"RM{patient.id:05d}"
    db.session.commit()

    return patient


def get_or_create_queue(patient, kind, number, priority, status):
    queue = QueueEntry.query.filter_by(number=number).first()

    if queue:
        return queue

    queue = QueueEntry(
        patient_id=patient.id,
        kind=kind,
        number=number,
        priority=priority,
        status=status
    )

    db.session.add(queue)
    db.session.commit()

    return queue


def create_visit_if_not_exists(patient, queue, doctor, diagnosis, notes, prescription_data):
    existing_visit = Visit.query.filter_by(
        patient_id=patient.id,
        diagnosis=diagnosis
    ).first()

    if existing_visit:
        return existing_visit

    visit = Visit(
        queue_id=queue.id,
        patient_id=patient.id,
        doctor_id=doctor.id,
        diagnosis=diagnosis,
        notes=notes
    )

    db.session.add(visit)
    db.session.flush()

    prescription = Prescription(
        visit_id=visit.id
    )

    db.session.add(prescription)
    db.session.flush()

    for medicine, qty in prescription_data:
        item = PrescriptionItem(
            prescription_id=prescription.id,
            medicine_id=medicine.id,
            qty=qty
        )

        if medicine.stock >= qty:
            medicine.stock -= qty

        db.session.add(item)

    queue.status = "done"

    db.session.commit()

    return visit


def create_audit_log(user, action, module, details):
    existing_log = AuditLog.query.filter_by(
        user_id=user.id,
        action=action,
        module=module
    ).first()

    if existing_log:
        return existing_log

    log = AuditLog(
        user_id=user.id,
        action=action,
        module=module,
        record_id=None,
        details=details,
        ip_address="127.0.0.1",
        user_agent="Demo Seeder"
    )

    db.session.add(log)
    db.session.commit()

    return log


with app.app_context():
    db.create_all()

    admin = get_or_create_user(
        name="Admin Klinik",
        email="admin@clinic.local",
        role="admin",
        password="admin123"
    )

    doctor = get_or_create_user(
        name="Doctor Klinik",
        email="doctor@clinic.local",
        role="doctor",
        password="doctor123"
    )

    receptionist = get_or_create_user(
        name="Receptionist Klinik",
        email="reception@clinic.local",
        role="receptionist",
        password="reception123"
    )

    paracetamol = get_or_create_medicine(
        name="Paracetamol",
        unit="tablet",
        category="Analgesik",
        description="Obat penurun demam dan pereda nyeri.",
        stock=100
    )

    amoxicillin = get_or_create_medicine(
        name="Amoxicillin",
        unit="kapsul",
        category="Antibiotik",
        description="Antibiotik untuk infeksi bakteri.",
        stock=80
    )

    vitamin_c = get_or_create_medicine(
        name="Vitamin C",
        unit="tablet",
        category="Vitamin",
        description="Suplemen daya tahan tubuh.",
        stock=120
    )

    cetirizine = get_or_create_medicine(
        name="Cetirizine",
        unit="tablet",
        category="Antihistamin",
        description="Obat untuk gejala alergi.",
        stock=50
    )

    patient_1 = get_or_create_patient(
        name="Budi Santoso",
        birthdate="1998-01-15",
        gender="Laki-laki",
        phone="081234567890",
        address="Jakarta"
    )

    patient_2 = get_or_create_patient(
        name="Siti Aminah",
        birthdate="2000-05-20",
        gender="Perempuan",
        phone="081298765432",
        address="Bekasi"
    )

    patient_3 = get_or_create_patient(
        name="Andi Wijaya",
        birthdate="1995-11-10",
        gender="Laki-laki",
        phone="081222333444",
        address="Cikarang"
    )

    queue_1 = get_or_create_queue(
        patient=patient_1,
        kind="walkin",
        number="W001",
        priority=3,
        status="waiting"
    )

    queue_2 = get_or_create_queue(
        patient=patient_2,
        kind="appointment",
        number="A001",
        priority=2,
        status="waiting"
    )

    queue_3 = get_or_create_queue(
        patient=patient_3,
        kind="emergency",
        number="E001",
        priority=1,
        status="waiting"
    )

    completed_queue = get_or_create_queue(
        patient=patient_1,
        kind="walkin",
        number="W999",
        priority=3,
        status="done"
    )

    create_visit_if_not_exists(
        patient=patient_1,
        queue=completed_queue,
        doctor=doctor,
        diagnosis="Demam ringan dan sakit kepala.",
        notes="Pasien disarankan istirahat cukup dan minum air putih.",
        prescription_data=[
            (paracetamol, 5),
            (vitamin_c, 3)
        ]
    )

    create_audit_log(
        user=admin,
        action="DEMO DATA CREATED",
        module="demo",
        details="Demo data was created for final presentation."
    )

    create_audit_log(
        user=receptionist,
        action="CREATE PATIENT DEMO",
        module="patients",
        details="Receptionist demo activity."
    )

    create_audit_log(
        user=doctor,
        action="CREATE EXAMINATION DEMO",
        module="doctor",
        details="Doctor demo activity."
    )

    print("Demo data has been created successfully.")
    print("Default accounts:")
    print("Admin        : admin@clinic.local / admin123")
    print("Doctor       : doctor@clinic.local / doctor123")
    print("Receptionist : reception@clinic.local / reception123")