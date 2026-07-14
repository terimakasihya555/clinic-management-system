# Clinic Management System

## 1. Project Overview

Clinic Management System is a web-based application developed using Flask to support clinic operational activities. The system integrates patient registration, queue management, doctor examination, prescription management, medicine inventory, medical record history, audit log, and user role management into one application.

This application was developed to improve clinic workflow by reducing manual work, improving data consistency, and supporting better access control for different user roles.

## 2. Main Features

### Authentication and Role Access

- Login system for multiple user roles.
- Available roles:
  - Admin
  - Doctor
  - Receptionist
- Each role has different access rights.
- Admin can manage user accounts and roles.
- The active admin account cannot delete itself or change its own role.

### Patient Management

- Add patient data.
- Search patient data.
- Generate medical record number automatically.
- Create queue from patient data.
- Access medical record history for Admin and Doctor.

### Queue Management

- Queue types:
  - Emergency
  - Appointment
  - Walk-in
- Queue priority:
  1. Emergency
  2. Appointment
  3. Walk-in
- Queue status:
  - Waiting
  - Serving
  - Done
- Queue monitor display for clinic screen.
- Auto-refresh queue display.

### Doctor Examination

- Doctor can view waiting patients.
- Doctor can call patients.
- Doctor can input diagnosis and medical notes.
- Doctor can create prescriptions during examination.

### Prescription and Stock Reduction

- Doctor can select medicine and prescription quantity.
- Medicine stock is automatically reduced after prescription is saved.
- The system rejects prescriptions if medicine stock is insufficient.

### Inventory and Stock Opname

- Add medicine data.
- Edit medicine data.
- Search and filter medicine.
- Stock opname for stock in and stock out.
- Stock status badge:
  - Safe
  - Low Stock
  - Empty Stock

### Medical Record History

- Admin and Doctor can view patient medical records.
- Medical record history includes:
  - Visit date
  - Doctor name
  - Diagnosis
  - Medical notes
  - Prescription history

### Audit Log

- The system records data-changing activities.
- Logged activities include POST, PUT, PATCH, and DELETE requests.
- Audit log contains:
  - User
  - Role
  - Action
  - Module
  - IP Address
  - User Agent
  - Timestamp

### User Management

- Admin can view user list.
- Admin can add new users.
- Admin can edit user information and role.
- Admin can delete other users.
- Password is stored using hashing.

### Security Features

- Password hashing.
- Role-based access control.
- Session timeout.
- Security headers.
- Simple rate limiting.
- Configurable IP restriction.
- Anti-copy script.
- Custom error pages for 403, 404, and 500.

## 3. Technology Stack

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite
- Bootstrap 5
- Jinja2
- Pytest
- Git and GitHub

## 4. Project Structure

```text
clinic-management-system/
├── clinic_app/
│   ├── blueprints/
│   │   ├── auth/
│   │   ├── patients/
│   │   ├── queue/
│   │   ├── doctor/
│   │   ├── inventory/
│   │   ├── audit/
│   │   └── users/
│   ├── models/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── auth/
│   │   ├── patients/
│   │   ├── queue/
│   │   ├── doctor/
│   │   ├── inventory/
│   │   ├── audit/
│   │   ├── users/
│   │   └── errors/
│   ├── __init__.py
│   └── security.py
├── docs/
│   ├── USER_ROLE_MATRIX.md
│   ├── TEST_CASES.md
│   ├── SYSTEM_FEATURE_SUMMARY.md
│   └── SECURITY_IMPLEMENTATION.md
├── tests/
│   ├── conftest.py
│   ├── test_basic.py
│   ├── test_auth.py
│   └── test_security.py
├── config.py
├── run.py
├── wsgi.py
├── requirements.txt
└── README.md
```

## 5. Installation

Clone the repository:

```bash
git clone <repository-url>
cd clinic-management-system
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment on Windows:

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

## 6. Default Login Account

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

## 7. Testing

Automated testing is implemented using Pytest.

Run the test:

```bash
pytest
```

Current test result:

```text
11 passed
```

The automated tests cover:

- Login page availability.
- Dashboard access protection.
- Public queue display page.
- Invalid route / 404 page.
- Admin login.
- Invalid login.
- Doctor role restriction.
- Admin access to user management.
- Security headers.
- Unauthenticated user redirect.
- Custom error page response.

## 8. Documentation

Additional documentation is available in the `docs` folder:

- `USER_ROLE_MATRIX.md` — describes access rights for Admin, Doctor, and Receptionist.
- `TEST_CASES.md` — summarizes manual and automated test scenarios.
- `SYSTEM_FEATURE_SUMMARY.md` — explains the main modules and system benefits.
- `SECURITY_IMPLEMENTATION.md` — explains the implemented security mechanisms.

## 9. Security Notes

For local development, IP restriction is disabled:

```python
ENABLE_IP_RESTRICTION = False
```

For deployment inside clinic network, IP restriction can be enabled by changing it to:

```python
ENABLE_IP_RESTRICTION = True
```

Allowed IP prefixes can be adjusted in `config.py`.

When using HTTPS in production, set:

```python
SESSION_COOKIE_SECURE = True
```

The system also includes security headers, session timeout, role-based access control, password hashing, and audit logging to improve data protection and accountability.

## 10. Thesis Relevance

This application supports clinic operational workflow through integrated modules, including patient registration, queue priority management, doctor examination, prescription management, stock control, medical record history, audit trail, and role-based access control.

The system applies the MVC concept through:

- Model: database entities using SQLAlchemy.
- View: HTML templates using Jinja2 and Bootstrap.
- Controller: Flask routes and blueprints.

The security implementation includes authentication, authorization, password hashing, session timeout, audit logging, input validation, security headers, and configurable IP restriction.

This project can be used as a practical implementation of a web-based clinic management system that focuses on usability, data management, access control, and operational efficiency.