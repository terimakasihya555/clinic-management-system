# Thesis Chapter 4 Material - Implementation and Result

## 1. System Implementation Overview

The Clinic Management System was successfully implemented as a Flask-based web application. The system provides integrated modules for patient management, queue management, doctor examination, prescription, inventory, medical record history, audit log, user management, security, testing, and deployment preparation.

The implementation follows a modular structure using Flask Blueprints. Each major feature is separated into its own blueprint to improve maintainability.

## 2. Authentication and Role Implementation

The system implements login functionality using Flask-Login. Users must log in before accessing protected pages.

The system has three roles:

| Role | Access Focus |
|---|---|
| Admin | System management, user management, audit log, all modules |
| Doctor | Examination, prescription, medical record |
| Receptionist | Patient registration, queue creation, stock opname |

Unauthorized users are prevented from accessing restricted pages. If a logged-in user attempts to access a page outside their role permission, the system displays a 403 Forbidden page.

## 3. Dashboard Implementation

The dashboard displays summary information such as:

- Total patients
- Waiting queue
- Serving queue
- Low stock medicine
- Recent activities

This helps users monitor clinic operations from one page.

## 4. Patient Management Implementation

The patient module allows authorized users to add and search patient data. The system automatically generates a medical record number after a patient is created.

Example medical record format:

```text
RM00001
```

Admin and Doctor can access patient medical record history. Receptionist can manage patient registration but cannot access detailed medical record history.

## 5. Queue Management Implementation

The queue module supports three queue types:

1. Emergency
2. Appointment
3. Walk-in

The system assigns priority values automatically:

| Queue Type | Priority |
|---|---:|
| Emergency | 1 |
| Appointment | 2 |
| Walk-in | 3 |

The queue list is sorted by priority and creation time. This ensures that emergency patients are served first.

## 6. Queue Monitor Implementation

The queue monitor page is designed for clinic display screens. It shows:

- Currently served queue number
- Next queue numbers
- Patient name
- Queue type
- Current time
- Auto-refresh every few seconds

This feature helps patients monitor the queue status clearly.

## 7. Doctor Examination Implementation

The doctor module allows doctors to:

- View waiting patients
- Call a patient
- Input diagnosis
- Input medical notes
- Add prescription
- Save examination result

After the examination is saved, the queue status changes to done and the visit record is stored in the database.

## 8. Prescription and Stock Reduction Implementation

The prescription module is integrated with the medicine inventory module.

When a doctor saves a prescription:

1. The system checks medicine stock.
2. If stock is sufficient, the prescription is saved.
3. Medicine stock is reduced automatically.
4. If stock is insufficient, the system rejects the transaction.

This prevents stock inconsistency and reduces manual calculation.

## 9. Inventory and Stock Opname Implementation

The inventory module supports:

- Add medicine
- Edit medicine
- Delete medicine with validation
- Search medicine
- Filter medicine by stock status
- Stock opname in
- Stock opname out

Medicine stock status is displayed using badges:

| Status | Condition |
|---|---|
| Safe | Stock above 10 |
| Low Stock | Stock between 1 and 10 |
| Empty | Stock 0 or below |

## 10. Medical Record History Implementation

The medical record module displays patient visit history. Each record includes:

- Visit date
- Doctor name
- Diagnosis
- Medical notes
- Prescription history

This feature helps doctors review previous patient treatment information.

## 11. Audit Log Implementation

The audit log module records data-changing activities such as POST, PUT, PATCH, and DELETE requests.

The log stores:

- User
- Action
- Module
- IP address
- User agent
- Timestamp

This supports monitoring and accountability.

## 12. User Management Implementation

Admin can manage user accounts through the User Management module.

Implemented features:

- View user list
- Add user
- Edit user
- Change role
- Delete user
- Prevent active admin from deleting itself
- Prevent active admin from changing its own role

This prevents accidental loss of admin access.

## 13. Security Implementation Result

The system includes the following security features:

- Password hashing
- Role-based access control
- Session timeout
- Security headers
- Simple rate limiting
- IP restriction configuration
- Audit logging
- Custom error pages
- Anti-copy script

The security implementation helps protect system access and sensitive data.

## 14. Testing Result

Automated testing was performed using Pytest.

Current test result:

```text
11 passed
```

The tests cover:

- Login page
- Dashboard protection
- 404 page
- Queue display page
- Admin login
- Invalid login
- Doctor role restriction
- Admin access to user management
- Security headers
- Unauthenticated redirect
- Custom error page response

## 15. Deployment Preparation Result

The system includes deployment preparation files:

| File | Function |
|---|---|
| `serve.py` | Runs application using Waitress |
| `start_local.bat` | Starts development server on Windows |
| `start_production.bat` | Starts production server on Windows |
| `backup_database.bat` | Creates SQLite database backup |
| `.env.example` | Provides environment variable example |

This makes the application easier to run on another computer or in a clinic local network.

## 16. Implementation Conclusion

The Clinic Management System was successfully implemented with complete modules for clinic operations. The system supports patient registration, queue priority, doctor examination, prescription, stock management, medical record history, audit log, user management, security, testing, and deployment preparation.

The result shows that the system can improve clinic workflow, reduce manual processes, support better data consistency, and provide role-based access control.