# Thesis Explanation

This document summarizes the system explanation for thesis writing and presentation.

## 1. System Overview

Clinic Management System is a web-based application designed to support clinic operational activities. The system helps manage patient registration, queue process, doctor examination, prescription, medicine inventory, medical record history, audit log, and user access control.

The application was developed using Flask as the web framework, SQLAlchemy as the ORM, SQLite as the database, and Bootstrap as the user interface framework.

The system focuses on improving clinic workflow by integrating several operational modules into one application.

## 2. Background of the System

In many small clinics, patient registration, queue management, medical records, and inventory are often handled manually or separately. This can cause problems such as:

- Inefficient patient registration.
- Unclear queue priority.
- Manual stock calculation.
- Difficulty in tracking medical history.
- Limited user activity monitoring.
- Risk of unauthorized access to sensitive data.

Therefore, this system was developed to provide an integrated solution for clinic management.

## 3. System Objective

The objectives of the system are:

1. To develop a web-based clinic management system.
2. To manage patient data and medical record history.
3. To implement priority-based queue management.
4. To support doctor examination and prescription.
5. To integrate prescription with medicine stock reduction.
6. To provide audit logging for user activities.
7. To implement role-based access control.
8. To prepare the system for local deployment.

## 4. Reason for Choosing Flask

Flask was selected because it is lightweight, flexible, and suitable for developing a modular web application.

Flask allows the system to be developed using blueprints, which helps separate each module such as:

- Authentication
- Patient management
- Queue management
- Doctor examination
- Inventory
- Audit log
- User management

Compared to heavier frameworks, Flask is easier to customize and suitable for a student project that requires clear structure and maintainable code.

## 5. Reason for Using SQLAlchemy

SQLAlchemy was used as the Object Relational Mapper. It helps the application interact with the database using Python classes instead of writing raw SQL queries manually.

The advantages of SQLAlchemy are:

- Easier database management.
- Better code readability.
- Easier relationship mapping between tables.
- Reduces repetitive SQL code.
- Supports safer query handling.

Examples of models in the system:

- User
- Patient
- QueueEntry
- Visit
- Medicine
- Prescription
- PrescriptionItem
- AuditLog

## 6. MVC Implementation

The system applies the MVC concept as follows.

### Model

The Model represents database entities using SQLAlchemy.

Examples:

- User
- Patient
- QueueEntry
- Visit
- Medicine
- Prescription
- PrescriptionItem
- AuditLog

### View

The View is implemented using Jinja2 HTML templates and Bootstrap.

Examples:

- Login page
- Dashboard page
- Patient list
- Queue monitor
- Doctor examination form
- Inventory page
- Audit log page
- User management page
- Medical record page

### Controller

The Controller is implemented using Flask routes and blueprints.

Examples:

- `auth` blueprint handles login and logout.
- `patients` blueprint handles patient data and medical records.
- `queue` blueprint handles queue creation and queue display.
- `doctor` blueprint handles examination and prescription.
- `inventory` blueprint handles medicine stock.
- `audit` blueprint handles audit log.
- `users` blueprint handles user management.

## 7. System Modules

### Authentication Module

This module manages user login and logout. The system uses Flask-Login for session management.

User roles include:

- Admin
- Doctor
- Receptionist

### Dashboard Module

The dashboard provides summary information such as total patients, queue status, low stock medicine, and recent activities.

### Patient Management Module

This module allows authorized users to add, search, and manage patient data. The system automatically generates medical record numbers.

### Queue Management Module

This module manages patient queues based on priority. The system supports emergency, appointment, and walk-in queues.

### Doctor Examination Module

This module allows doctors to call patients, input diagnosis, write medical notes, and save examination results.

### Prescription Module

This module allows doctors to create prescriptions during examination. The system validates medicine stock before saving prescription data.

### Inventory Module

This module manages medicine data and stock opname. It supports stock in, stock out, stock status filter, and low stock indicators.

### Medical Record Module

This module stores and displays patient visit history, diagnosis, medical notes, doctor information, and prescription history.

### Audit Log Module

This module records data-changing activities performed by users. It supports system monitoring and accountability.

### User Management Module

This module allows Admin to manage user accounts and roles.

## 8. Queue Priority Logic

The queue system supports three queue types:

1. Emergency
2. Appointment
3. Walk-in

Emergency patients receive the highest priority. Appointment patients are prioritized after emergency patients, and walk-in patients are served after appointment patients.

The queue is ordered by priority and creation time. This ensures that urgent cases are handled first while maintaining fairness based on arrival time.

Priority order:

```text
Emergency → Appointment → Walk-in
```

## 9. Prescription and Stock Integration

The prescription module is integrated with the inventory module. When a doctor saves a prescription, the system checks whether the selected medicine has sufficient stock.

If the stock is sufficient, the system saves the prescription and automatically reduces the medicine stock.

If the stock is insufficient, the system rejects the prescription and shows an error message.

This integration helps reduce manual stock calculation and prevents medicine stock inconsistency.

## 10. Medical Record History

The medical record module stores patient visit history. Each record includes:

- Visit date
- Doctor name
- Diagnosis
- Medical notes
- Prescription history

Admin and Doctor can access medical record history, while Receptionist is restricted from viewing detailed medical records to protect sensitive patient information.

## 11. Role-Based Access Control

The system uses role-based access control to limit user access based on responsibilities.

Roles:

- Admin
- Doctor
- Receptionist

Admin has full access to system management features. Doctor can access examination and medical records. Receptionist can manage patient registration and queue creation.

Unauthorized users receive a 403 Forbidden response.

## 12. Security Implementation

The system includes several security mechanisms:

- Password hashing
- Login session management
- Role-based access control
- Session timeout
- Security headers
- Simple rate limiting
- Configurable IP restriction
- Anti-copy script
- Audit logging
- Custom error pages

These security features help protect user access, reduce unauthorized actions, and improve accountability.

## 13. Audit Log

Audit log records data-changing activities in the system. The log includes:

- User information
- Action
- Module
- IP address
- User agent
- Timestamp

Audit log helps system administrators monitor user activities and investigate operational changes.

## 14. Testing

Testing was performed using manual testing and automated testing with Pytest.

Automated tests cover:

- Login page
- Dashboard access protection
- 404 page
- Queue display page
- Admin login
- Invalid login
- Role restriction
- Security headers

The latest automated test result shows:

```text
11 passed
```

## 15. Deployment

The system can be run locally using Flask development server or in production mode using Waitress.

The project includes:

- `serve.py`
- `start_local.bat`
- `start_production.bat`
- `backup_database.bat`
- `.env.example`
- Deployment guide documentation

This supports deployment on a clinic computer or local network.

## 16. System Benefits

The system provides several benefits:

1. Improves patient registration process.
2. Provides priority-based queue management.
3. Helps doctors record examination results.
4. Connects prescription with medicine inventory.
5. Reduces manual stock calculation.
6. Stores patient medical history.
7. Supports user activity monitoring.
8. Improves access control based on user roles.
9. Supports local deployment for clinic use.

## 17. Limitation

The current system is designed for local or small clinic network usage. It uses SQLite database, which is suitable for lightweight deployment.

For larger scale usage, the system can be improved by using a more powerful database such as PostgreSQL or MySQL and deploying it with HTTPS and server infrastructure.

## 18. Conclusion

The Clinic Management System successfully integrates major clinic operational workflows into one web-based application. It supports patient data management, queue prioritization, doctor examination, prescription, inventory control, medical record history, audit monitoring, and role-based security.

The system improves efficiency, reduces manual work, supports data consistency, and provides better access control for clinic operations.