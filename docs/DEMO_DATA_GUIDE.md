# Demo Data Guide

This document explains how to create demo data for the Clinic Management System.

## 1. Purpose

Demo data is used to prepare the application for presentation or testing. It helps demonstrate system features without manually inputting data from the beginning.

The demo data includes:

- Default users
- Sample patients
- Sample medicines
- Sample queue data
- Sample medical record
- Sample prescription
- Sample audit log

## 2. Demo Accounts

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

## 3. Sample Patients

The demo data includes sample patients such as:

| No | Patient Name | Queue Type |
|---:|---|---|
| 1 | Budi Santoso | Walk-in |
| 2 | Siti Aminah | Appointment |
| 3 | Andi Wijaya | Emergency |

These patients can be used to demonstrate queue priority.

## 4. Sample Medicines

The demo data includes sample medicines:

| No | Medicine | Category |
|---:|---|---|
| 1 | Paracetamol | Analgesik |
| 2 | Amoxicillin | Antibiotik |
| 3 | Vitamin C | Vitamin |
| 4 | Cetirizine | Antihistamin |

These medicines can be used to demonstrate prescription and stock reduction.

## 5. How to Create Demo Data

Run this command:

```bash
python seed_demo_data.py
```

Or double-click:

```text
seed_demo_data.bat
```

## 6. After Running Demo Seeder

After the script runs successfully, open the application:

```bash
python run.py
```

Then open browser:

```text
http://127.0.0.1:5000
```

## 7. Demo Flow Using Seeded Data

Recommended demo flow:

1. Login as Receptionist.
2. Open patient page.
3. Show sample patients.
4. Open queue page.
5. Show emergency, appointment, and walk-in queue.
6. Open queue monitor.
7. Login as Doctor.
8. Call patient.
9. Fill examination and prescription.
10. Login as Admin.
11. Open inventory to show stock reduction.
12. Open medical record history.
13. Open audit log.

## 8. Important Notes

The demo data script is designed to avoid duplicate data as much as possible. If the same user, medicine, or patient already exists, the script will reuse existing data.

For a clean demo, the database can be backed up first using:

```text
backup_database.bat
```

## 9. Conclusion

The demo data helps prepare the Clinic Management System for presentation. It supports a complete demonstration of patient registration, queue priority, doctor examination, prescription, inventory, medical record history, and audit log.