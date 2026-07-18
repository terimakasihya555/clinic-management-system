# Clinic Management System

## 1. Project Overview

Clinic Management System is a web-based application developed using Flask to support clinic operational activities. The system integrates patient registration, priority-based queue management, doctor examination, prescription management, medicine inventory, medical record history, audit log, user management, reporting, security, testing, and deployment preparation into one application.

This application was developed to improve clinic workflow by reducing manual work, improving data consistency, supporting role-based access control, and providing a more structured operational process for small clinic environments.

The system is designed for local or clinic-network deployment, where staff can access the application through a browser while the application runs on a server computer or local machine.

---

## 2. Main Features

The Clinic Management System provides the following main features:

1. User authentication and login system.
2. Role-based access control for Admin, Doctor, and Receptionist.
3. Patient registration and patient data management.
4. Patient edit feature for Admin and Receptionist.
5. Automatic medical record number generation.
6. Priority-based queue management for Emergency, Appointment, and Walk-in patients.
7. Queue monitor display for clinic screen.
8. Doctor examination module.
9. Diagnosis and medical notes input.
10. Prescription management.
11. Automatic medicine stock reduction after prescription.
12. Medicine inventory management.
13. Stock opname for stock in and stock out.
14. Medical record history.
15. Medical record print feature.
16. Excel export for patient data.
17. Excel export for medical records.
18. Excel export for medicine inventory.
19. Excel export for audit logs.
20. Audit log for user activity monitoring.
21. User management for Admin.
22. Password hashing.
23. Session timeout.
24. Security headers.
25. Simple rate limiting.
26. Optional IP restriction for clinic network deployment.
27. Anti-copy script.
28. Custom error pages for 403, 404, and 500.
29. Environment-based configuration using `.env`.
30. Production logging using rotating log files.
31. Health check endpoint for production monitoring.
32. Automated testing using Pytest.
33. Local and production deployment support using Flask and Waitress.
34. Windows launcher files for easier application startup.
35. Database backup script.
36. Demo data seeder for presentation and testing.

---

## 3. User Roles

The system has three main user roles:

| Role | Description |
|---|---|
| Admin | Manages users, patients, inventory, audit log, reports, and system data. |
| Doctor | Handles patient examination, diagnosis, prescription, and medical record review. |
| Receptionist | Handles patient registration, queue creation, and stock opname support. |

Access to each module is controlled using role-based access control. Users can only access features that match their responsibility.

---

## 4. Technology Stack

The system was developed using:

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- Jinja2
- Bootstrap 5
- OpenPyXL
- Python-dotenv
- Pytest
- Waitress
- Git and GitHub

---

## 5. Project Structure

```text
clinic-management-system/
├── clinic_app/
│   ├── blueprints/
│   │   ├── audit/
│   │   ├── auth/
│   │   ├── doctor/
│   │   ├── health/
│   │   ├── inventory/
│   │   ├── patients/
│   │   ├── queue/
│   │   └── users/
│   ├── models/
│   │   ├── audit_log.py
│   │   ├── medicine.py
│   │   ├── patient.py
│   │   ├── prescription.py
│   │   ├── queue.py
│   │   ├── user.py
│   │   ├── visit.py
│   │   └── __init__.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── audit/
│   │   ├── auth/
│   │   ├── doctor/
│   │   ├── errors/
│   │   ├── inventory/
│   │   ├── patients/
│   │   ├── queue/
│   │   └── users/
│   ├── utils/
│   │   ├── export_excel.py
│   │   ├── logging_config.py
│   │   ├── time.py
│   │   └── __init__.py
│   ├── __init__.py
│   └── security.py
├── docs/
│   ├── DEMO_DATA_GUIDE.md
│   ├── DEMO_SCRIPT.md
│   ├── DEPLOYMENT_GUIDE.md
│   ├── FINAL_DEMO_CHECKLIST.md
│   ├── FINAL_FEATURE_LIST.md
│   ├── MVC_ARCHITECTURE_EXPLANATION.md
│   ├── SECURITY_IMPLEMENTATION.md
│   ├── SYSTEM_FEATURE_SUMMARY.md
│   ├── TEST_CASES.md
│   ├── TESTING_AND_EVALUATION_SUMMARY.md
│   ├── THESIS_CHAPTER_3_MATERIAL.md
│   ├── THESIS_CHAPTER_4_MATERIAL.md
│   ├── THESIS_EXPLANATION.md
│   └── USER_ROLE_MATRIX.md
├── tests/
│   ├── conftest.py
│   ├── test_auth.py
│   ├── test_basic.py
│   ├── test_health.py
│   ├── test_phase_22_23_features.py
│   └── test_security.py
├── .env.example
├── .gitignore
├── backup_database.bat
├── config.py
├── requirements.txt
├── run.py
├── seed_demo_data.py
├── seed_demo_data.bat
├── serve.py
├── start_local.bat
├── start_production.bat
├── wsgi.py
└── README.md
```

---

## 6. Installation

Clone the repository:

```bash
git clone https://github.com/terimakasihya555/clinic-management-system.git
cd clinic-management-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate.bat
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python run.py
```

Open the application in browser:

```text
http://127.0.0.1:5000
```

---

## 7. Environment Configuration

The application supports environment-based configuration using `.env`.

The project provides `.env.example` as a template:

```env
APP_VERSION=1.0.0

SECRET_KEY=change-this-secret-key

DATABASE_URL=sqlite:///clinic.sqlite

ENABLE_IP_RESTRICTION=False
ALLOWED_IP_PREFIXES=127.,192.168.,10.

RATE_LIMIT_MAX_REQUESTS=200
RATE_LIMIT_WINDOW_SECONDS=60
SESSION_TIMEOUT_MINUTES=30

SESSION_COOKIE_SECURE=False
```

For production deployment, create a `.env` file based on `.env.example` and adjust the values according to the deployment environment.

The real `.env` file must not be uploaded to GitHub.

---

## 8. Default Login Account

### Admin

```text
Email    : admin@clinic.local
Password : admin123
```

### Doctor

```text
Email    : doctor@clinic.local
Password : doctor123
```

### Receptionist

```text
Email    : reception@clinic.local
Password : reception123
```

For real deployment, default passwords should be changed immediately.

---

## 9. Testing

Automated testing is implemented using Pytest.

Run the test:

```bash
pytest
```

Final automated test result:

```text
18 passed, 0 warnings
```

The automated tests cover:

- Login page access.
- Admin login.
- Invalid login.
- Dashboard protection.
- Role-based access restriction.
- Queue display access.
- 404 error page.
- Security headers.
- Patient update feature.
- Patient Excel export.
- Medical record Excel export.
- Inventory Excel export.
- Audit log Excel export.
- Health check endpoint.

---

## 10. Production Readiness

This project includes several production readiness features:

- Waitress production server support.
- Environment-based configuration using `.env`.
- Rotating production log file.
- Health check endpoint.
- Database backup script.
- Security headers.
- Session timeout.
- Rate limiting.
- Optional IP restriction for local clinic network deployment.
- Warning cleanup for deprecated datetime and SQLAlchemy query usage.

The health check endpoint can be accessed at:

```text
http://127.0.0.1:5000/health/
```

Example response:

```json
{
  "app": "Clinic Management System",
  "database": "connected",
  "status": "ok",
  "version": "1.0.0"
}
```

Production logs are stored in:

```text
logs/clinic_app.log
```

The `logs/` folder is excluded from Git using `.gitignore`.

---

## 11. Documentation

Additional documentation is available in the `docs` folder:

- `USER_ROLE_MATRIX.md` — describes access rights for Admin, Doctor, and Receptionist.
- `TEST_CASES.md` — summarizes manual and automated test scenarios.
- `SYSTEM_FEATURE_SUMMARY.md` — explains the main modules and system benefits.
- `SECURITY_IMPLEMENTATION.md` — explains the implemented security mechanisms.
- `DEPLOYMENT_GUIDE.md` — explains how to run and deploy the system.
- `DEMO_SCRIPT.md` — provides the system demonstration flow.
- `FINAL_DEMO_CHECKLIST.md` — provides a checklist before final demonstration.
- `FINAL_FEATURE_LIST.md` — lists all final implemented features.
- `THESIS_EXPLANATION.md` — explains the system in thesis context.
- `DEMO_DATA_GUIDE.md` — explains how to create sample data for demo.
- `THESIS_CHAPTER_3_MATERIAL.md` — provides thesis Chapter 3 material.
- `THESIS_CHAPTER_4_MATERIAL.md` — provides thesis Chapter 4 material.
- `MVC_ARCHITECTURE_EXPLANATION.md` — explains the MVC structure.
- `TESTING_AND_EVALUATION_SUMMARY.md` — summarizes testing and evaluation.

---

## 12. Security Notes

For local development, IP restriction is disabled:

```env
ENABLE_IP_RESTRICTION=False
```

For deployment inside clinic network, IP restriction can be enabled:

```env
ENABLE_IP_RESTRICTION=True
```

Allowed IP prefixes can be adjusted:

```env
ALLOWED_IP_PREFIXES=127.,192.168.,10.
```

When using HTTPS in production, set:

```env
SESSION_COOKIE_SECURE=True
```

The system also includes:

- Password hashing.
- Authentication.
- Role-based authorization.
- Session timeout.
- Audit logging.
- Input validation.
- Security headers.
- Rate limiting.
- Optional IP restriction.
- Custom error pages.

These security mechanisms help improve access control, accountability, and application reliability.

---

## 13. Thesis Relevance

This application supports clinic operational workflow through integrated modules, including patient registration, queue priority management, doctor examination, prescription management, stock control, medical record history, audit trail, reporting, and role-based access control.

The system applies the MVC concept through:

- Model: database entities using SQLAlchemy.
- View: HTML templates using Jinja2 and Bootstrap.
- Controller: Flask routes and blueprints.

The system also includes security hardening, testing, deployment preparation, production logging, and health check support. These elements show that the project is not only focused on application functionality, but also maintainability, reliability, and readiness for real-world usage.

---

## 14. Conclusion

Clinic Management System is a complete web-based application for small clinic operational management. It integrates registration, queue handling, examination, prescription, inventory, medical record, audit log, user management, security, reporting, testing, and deployment preparation.

The project is suitable for academic demonstration, thesis implementation, and GitHub portfolio presentation.