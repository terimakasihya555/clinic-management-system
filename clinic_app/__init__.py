from flask import Flask, redirect, url_for, render_template
from flask_login import LoginManager, current_user, login_required
from werkzeug.security import generate_password_hash

from config import Config
from clinic_app.models import db
from clinic_app.models.user import User
from clinic_app.models.medicine import Medicine
from clinic_app.models.patient import Patient
from clinic_app.models.queue import QueueEntry
from clinic_app.models.audit_log import AuditLog
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

    from clinic_app.blueprints.users.routes import users_bp
    from clinic_app.blueprints.auth.routes import auth_bp
    from clinic_app.blueprints.patients.routes import patients_bp
    from clinic_app.blueprints.queue.routes import queue_bp
    from clinic_app.blueprints.doctor.routes import doctor_bp
    from clinic_app.blueprints.inventory.routes import inventory_bp
    from clinic_app.blueprints.audit.routes import audit_bp

    app.register_blueprint(users_bp)
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
        return redirect(url_for("dashboard"))

    @app.route("/dashboard")
    @login_required
    def dashboard():
        total_patients = Patient.query.count()
        waiting_queue = QueueEntry.query.filter_by(status="waiting").count()
        serving_queue = QueueEntry.query.filter_by(status="serving").count()
        total_medicines = Medicine.query.count()
        low_stock = Medicine.query.filter(Medicine.stock <= 10).count()

        recent_logs = AuditLog.query.order_by(
            AuditLog.timestamp.desc()
        ).limit(5).all()

        stats = {
            "total_patients": total_patients,
            "waiting_queue": waiting_queue,
            "serving_queue": serving_queue,
            "total_medicines": total_medicines,
            "low_stock": low_stock,
        }

        return render_template(
            "dashboard.html",
            stats=stats,
            recent_logs=recent_logs
        )
        
    @app.errorhandler(403)
    def forbidden(error):
        return render_template("errors/403.html"), 403


    @app.errorhandler(404)
    def not_found(error):
        return render_template("errors/404.html"), 404


    @app.errorhandler(500)
    def internal_error(error):
        return render_template("errors/500.html"), 500

    with app.app_context():
        db.create_all()
        seed_data()

    return app


def seed_data():
    if not User.query.first():
        db.session.add_all([
            User(
                name="Admin Klinik",
                email="admin@clinic.local",
                role="admin",
                password_hash=generate_password_hash("admin123")
            ),
            User(
                name="Resepsionis Klinik",
                email="reception@clinic.local",
                role="receptionist",
                password_hash=generate_password_hash("reception123")
            ),
            User(
                name="Dokter Klinik",
                email="doctor@clinic.local",
                role="doctor",
                password_hash=generate_password_hash("doctor123")
            ),
        ])

    if not Medicine.query.first():
        db.session.add_all([
            Medicine(
                name="Paracetamol",
                unit="tablet",
                category="Analgesik",
                description="Obat demam",
                stock=100
            ),
            Medicine(
                name="Amoxicillin",
                unit="kapsul",
                category="Antibiotik",
                description="Antibiotik umum",
                stock=50
            ),
        ])

    db.session.commit()