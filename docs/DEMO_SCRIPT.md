# Demo Script

This document provides the application demo flow for the Clinic Management System.

## 1. Opening

Good morning/afternoon. In this demo, I will present the Clinic Management System, a web-based application developed using Flask to support clinic operational activities.

The system includes patient registration, queue management, doctor examination, prescription, inventory management, medical record history, audit log, and user role management.

The main purpose of this system is to integrate clinic operational processes into one web-based application so that the clinic can manage data more efficiently, consistently, and securely.

## 2. Login Demonstration

The system supports three user roles:

- Admin
- Doctor
- Receptionist

Each role has different access rights based on the responsibility of the user.

### Admin Account

```text
Email    : admin@clinic.local
Password : admin123
```

### Doctor Account

```text
Email    : doctor@clinic.local
Password : doctor123
```

### Receptionist Account

```text
Email    : reception@clinic.local
Password : reception123
```

## 3. Admin Demo Flow

Login as Admin.

Demonstrate the following features:

1. Open the dashboard page.
2. Show dashboard summary cards.
3. Open patient data page.
4. Open queue management page.
5. Open inventory page.
6. Open audit log page.
7. Open user management page.
8. Show medical record access.

Admin has the highest access because this role is responsible for managing the system, monitoring activity, and controlling user roles.

## 4. Receptionist Demo Flow

Login as Receptionist.

Demonstrate the following features:

1. Open dashboard.
2. Open patient data page.
3. Add new patient.
4. Search patient.
5. Create queue from patient data.
6. Open queue list.
7. Open queue monitor display.
8. Perform stock opname.

Receptionist focuses on patient registration, queue creation, and supporting inventory stock update.

## 5. Doctor Demo Flow

Login as Doctor.

Demonstrate the following features:

1. Open doctor dashboard.
2. View waiting patients.
3. Call patient.
4. Fill diagnosis.
5. Fill medical notes.
6. Add prescription.
7. Save examination.
8. Open patient medical record history.

Doctor focuses on medical examination, diagnosis, prescription, and medical record history.

## 6. Queue Priority Demo

Create three queue types:

1. Walk-in
2. Appointment
3. Emergency

The system should prioritize emergency patients first, followed by appointment patients, and then walk-in patients.

Queue priority order:

```text
Emergency → Appointment → Walk-in
```

This shows that the queue system supports priority-based service.

## 7. Queue Monitor Demo

Open the queue monitor page:

```text
/queue/display
```

Show that the page displays:

- Currently served queue number
- Next queue numbers
- Patient name
- Queue type
- Clock
- Auto-refresh display

This page is designed for a clinic display monitor.

## 8. Prescription and Stock Reduction Demo

During doctor examination:

1. Select medicine.
2. Input prescription quantity.
3. Save examination.
4. Open inventory page.
5. Show that medicine stock decreases automatically.

This proves that the prescription module is integrated with the inventory module.

If the prescription quantity is greater than available stock, the system will reject the transaction and show an error message.

## 9. Medical Record Demo

Open patient medical record.

Show the following information:

- Patient information
- Total visit
- Total prescription
- Visit history
- Doctor name
- Diagnosis
- Medical notes
- Prescription history

This shows that examination data is stored as patient medical record history.

## 10. Audit Log Demo

Login as Admin and open Audit Log.

Show that the system records user activities such as:

- Patient registration
- Queue creation
- Doctor examination
- Prescription creation
- Stock update
- User management action

Audit log includes:

- User
- Role
- Action
- Module
- IP address
- User agent
- Timestamp

This feature supports accountability and activity monitoring.

## 11. User Management Demo

Login as Admin and open User Management.

Demonstrate:

1. View user list.
2. Add new user.
3. Edit user data.
4. Change user role.
5. Delete another user.
6. Show that the active admin cannot delete itself.
7. Show that the active admin cannot change its own role.

This prevents the admin from accidentally losing access to the system.

## 12. Security Demo

Demonstrate role restriction:

1. Login as Doctor.
2. Try opening:

```text
/users/
```

3. The system shows 403 Forbidden page.

This proves that role-based access control is working.

Also explain that the system includes:

- Password hashing
- Session timeout
- Security headers
- Rate limiting
- IP restriction configuration
- Custom error pages
- Audit logging

## 13. Testing Demo

Show automated testing result using Pytest.

Run:

```bash
pytest
```

Current result:

```text
11 passed
```

This shows that basic system functionality and access control have been tested.

## 14. Deployment Demo

Explain that the system can run in two modes:

Development mode:

```bash
python run.py
```

Production mode using Waitress:

```bash
python serve.py
```

The system also provides Windows launcher files:

```text
start_local.bat
start_production.bat
backup_database.bat
```

This makes the system easier to run on another computer.

## 15. Closing

The Clinic Management System integrates clinic operational processes into one web-based application.

The system supports:

- Patient registration
- Queue priority management
- Doctor examination
- Prescription and automatic stock reduction
- Inventory management
- Medical record history
- Audit log
- User role management
- Security and access control
- Testing and deployment preparation

Overall, this system improves workflow efficiency, data consistency, access control, and monitoring in clinic operations.