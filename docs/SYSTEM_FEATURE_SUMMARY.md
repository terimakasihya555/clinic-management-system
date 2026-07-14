# System Feature Summary

Clinic Management System is a web-based application developed using Flask to support clinic operational activities.

## Main Modules

### 1. Authentication Module
The system provides login functionality for three roles: Admin, Doctor, and Receptionist. Passwords are stored using hashing to improve security.

### 2. Patient Management Module
This module allows authorized users to manage patient data. Patient medical record numbers are generated automatically after patient registration.

### 3. Queue Management Module
The queue system supports three types of queue:
1. Emergency
2. Appointment
3. Walk-in

The queue is prioritized based on urgency, where emergency patients receive the highest priority.

### 4. Queue Display Module
The queue display page is designed for a clinic monitor screen. It shows the currently served queue number and the next queue numbers. The display refreshes automatically.

### 5. Doctor Examination Module
Doctors can call patients, perform examinations, input diagnosis, and write medical notes.

### 6. Prescription Module
Doctors can create prescriptions during examination. The medicine stock is automatically reduced based on the prescribed quantity.

### 7. Inventory Module
The inventory module allows medicine management, including add, edit, delete, search, filter, and stock opname. The system also marks medicine stock as safe, low, or empty.

### 8. Medical Record Module
The system stores patient visit history, diagnosis, medical notes, doctor information, and prescription history. This module can be accessed by Admin and Doctor.

### 9. Audit Log Module
The system records user activities such as data creation, updates, and deletion actions. This supports accountability and monitoring.

### 10. User Management Module
Admin can manage users and assign roles. The system prevents the active admin account from deleting itself or changing its own role.

## System Benefits

The system improves clinic operations by integrating patient registration, queue management, examination, prescription, inventory, and medical record history into one application. It reduces manual work, improves data consistency, and supports better monitoring of user activities.