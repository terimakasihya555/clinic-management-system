from flask import Flask, redirect, url_for
from flask_login import LoginManager, current_user
from werkzeug.security import generate_password_hash
from config import Config
from clinic_app.models import db
from clinic_app.models.user import User
from clinic_app.models.medicine import Medicine
from clinic_app.security import init_security

login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    login_manager.init_app(app)
    init_security(app)

    from clinic_app.blueprints.auth.routes import auth_bp
    from clinic_app.blueprints.patients.routes import patients_bp
    from clinic_app.blueprints.queue.routes import queue_bp
    from clinic_app.blueprints.doctor.routes import doctor_bp
    from clinic_app.blueprints.inventory.routes import inventory_bp
    from clinic_app.blueprints.audit.routes import audit_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(patients_bp)
    app.register_blueprint(queue_bp)
    app.register_blueprint(doctor_bp)
    app.register_blueprint(inventory_bp)
    app.register_blueprint(audit_bp)

    @app.route("/")
    def index():
        if not current_user.is_authenticated:
            return redirect(url_for("auth.login"))
        if current_user.role == "doctor":
            return redirect(url_for("doctor.dashboard"))
        if current_user.role == "admin":
            return redirect(url_for("inventory.index"))
        return redirect(url_for("patients.index"))

    with app.app_context():
        db.create_all()
        seed_data()

    return app

def seed_data():
    if not User.query.first():
        db.session.add_all([
            User(name="Admin Klinik", email="admin@clinic.local", role="admin", password_hash=generate_password_hash("admin123")),
            User(name="Resepsionis Klinik", email="reception@clinic.local", role="receptionist", password_hash=generate_password_hash("reception123")),
            User(name="Dokter Klinik", email="doctor@clinic.local", role="doctor", password_hash=generate_password_hash("doctor123")),
        ])
    if not Medicine.query.first():
        db.session.add_all([
            Medicine(name="Paracetamol", unit="tablet", category="Analgesik", description="Obat demam", stock=100),
            Medicine(name="Amoxicillin", unit="kapsul", category="Antibiotik", description="Antibiotik umum", stock=50),
        ])
    db.session.commit()
