from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def load_models():
    from clinic_app.models.user import User
    from clinic_app.models.patient import Patient
    from clinic_app.models.queue import QueueEntry
    from clinic_app.models.visit import Visit
    from clinic_app.models.medicine import Medicine
    from clinic_app.models.prescription import Prescription, PrescriptionItem
    from clinic_app.models.audit_log import AuditLog

    return [
        User,
        Patient,
        QueueEntry,
        Visit,
        Medicine,
        Prescription,
        PrescriptionItem,
        AuditLog,
    ]