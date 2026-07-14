# Thesis Chapter 3 Material - System Design

## 1. System Development Approach

The Clinic Management System was developed as a web-based application using Flask. The system was designed to support clinic operational processes, including patient registration, queue management, doctor examination, prescription, medicine inventory, medical record history, audit log, and user management.

The development process focused on building a modular system structure. Each main function was separated into different modules using Flask Blueprints. This approach makes the application easier to maintain, test, and extend.

## 2. System Users

The system has three main user roles:

| Role | Description |
|---|---|
| Admin | Manages users, monitors audit logs, accesses all modules, and controls system data. |
| Doctor | Handles patient examination, diagnosis, prescription, and medical record access. |
| Receptionist | Handles patient registration, queue creation, and stock opname support. |

Each role has different access rights based on its responsibility.

## 3. Proposed System Workflow

The proposed system workflow starts from user login. After login, the user will be directed to the dashboard based on their role.

### Main Workflow

1. User logs in to the system.
2. Receptionist registers patient data.
3. Receptionist creates queue for the patient.
4. The system assigns queue priority based on queue type.
5. Doctor calls the patient from the doctor dashboard.
6. Doctor performs examination and inputs diagnosis.
7. Doctor adds prescription if needed.
8. The system reduces medicine stock automatically.
9. Medical record history is saved.
10. Admin can monitor activities through audit log.

## 4. Queue Priority Design

The system supports three types of queue:

1. Emergency
2. Appointment
3. Walk-in

The priority order is:

```text
Emergency → Appointment → Walk-in
```

Emergency patients have the highest priority because they require urgent treatment. Appointment patients are placed after emergency patients, while walk-in patients are served after appointment patients.

If two patients have the same priority, the system sorts them based on arrival time.

## 5. Database Design Overview

The system uses SQLite as the database and SQLAlchemy as the ORM.

Main database entities:

| Entity | Description |
|---|---|
| User | Stores user account data and role information. |
| Patient | Stores patient identity and medical record number. |
| QueueEntry | Stores queue number, queue type, priority, and status. |
| Visit | Stores doctor examination result. |
| Medicine | Stores medicine data and stock information. |
| Prescription | Stores prescription header linked to visit. |
| PrescriptionItem | Stores medicine items in a prescription. |
| AuditLog | Stores user activity records. |

## 6. MVC Design

The system applies the MVC concept.

| MVC Component | Implementation |
|---|---|
| Model | SQLAlchemy models inside `clinic_app/models` |
| View | Jinja2 templates inside `clinic_app/templates` |
| Controller | Flask routes and blueprints inside `clinic_app/blueprints` |

The MVC structure improves code organization and separates database logic, user interface, and application control flow.

## 7. Security Design

The system includes several security mechanisms:

- Login authentication
- Password hashing
- Role-based access control
- Session timeout
- Security headers
- Simple rate limiting
- Configurable IP restriction
- Audit logging
- Custom error pages
- Anti-copy script

These mechanisms are implemented to protect user access, reduce unauthorized actions, and improve system accountability.

## 8. Deployment Design

The system can be deployed locally or in a clinic local network. The project includes:

- `run.py` for development server
- `serve.py` for production server using Waitress
- `start_local.bat` for local launcher
- `start_production.bat` for production launcher
- `backup_database.bat` for database backup

This design allows the application to be used on a single computer or accessed by several devices in the same clinic network.