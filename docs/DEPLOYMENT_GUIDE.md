# Deployment Guide

This document explains how to prepare and run the Clinic Management System on another computer or clinic environment.

---

## 1. Requirements

The target computer should have:

- Python installed.
- Git installed.
- Internet connection for initial dependency installation.
- Web browser.
- Local network connection if the system will be accessed by multiple devices.

Recommended environment:

```text
Python 3.12 or later
Windows operating system
Google Chrome or Microsoft Edge browser
```

---

## 2. Clone Repository

Open Command Prompt and run:

```bash
git clone https://github.com/terimakasihya555/clinic-management-system.git
cd clinic-management-system
```

---

## 3. Create Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

---

## 4. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate.bat
```

After activation, the terminal should show:

```text
(venv) C:\path\to\clinic-management-system>
```

---

## 5. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

The main dependencies include:

- Flask
- Flask-SQLAlchemy
- Flask-Login
- Werkzeug
- Pytest
- Waitress
- OpenPyXL
- Python-dotenv

---

## 6. Environment Configuration

The application supports environment-based configuration using a `.env` file.

The repository provides this template:

```text
.env.example
```

Example configuration:

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

For real deployment, create a `.env` file based on `.env.example`.

Example:

```bash
copy .env.example .env
```

Then edit `.env` according to the deployment environment.

Important note:

```text
Do not upload the real .env file to GitHub.
```

---

## 7. Run in Local Development Mode

Run the application using Flask development server:

```bash
python run.py
```

Or double-click:

```text
start_local.bat
```

Open the application in browser:

```text
http://127.0.0.1:5000
```

---

## 8. Run in Production Mode

The application can be served using Waitress production server.

Run:

```bash
python serve.py
```

Or double-click:

```text
start_production.bat
```

Open the application in browser:

```text
http://127.0.0.1:5000
```

For local network access, the application runs on:

```text
0.0.0.0:5000
```

This allows other devices in the same network to access the system using the server computer IP address.

---

## 9. Access from Other Devices in the Same Network

If the clinic uses one computer as the server, other devices in the same WiFi or LAN can access the application using the server computer IP address.

Example:

```text
http://192.168.1.10:5000
```

The IP address depends on the network configuration.

To check the server computer IP address on Windows, open Command Prompt and run:

```bash
ipconfig
```

Look for the IPv4 Address, for example:

```text
IPv4 Address . . . . . . . . . . . : 192.168.1.10
```

Other devices in the same network can open:

```text
http://192.168.1.10:5000
```

---

## 10. Health Check

The system provides a health check endpoint:

```text
/health/
```

Local URL:

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

The health check endpoint verifies:

- The application is running.
- The database connection is available.
- The application version can be read from configuration.

This endpoint can be used during production monitoring or final deployment testing.

---

## 11. Production Logging

The system supports production logging using rotating log files.

Log location:

```text
logs/clinic_app.log
```

The logging system uses rotating file handling to prevent the log file from growing too large.

The `logs/` folder is excluded from Git using `.gitignore`, so log files are not uploaded to GitHub.

Production logging helps developers or administrators check application activity and identify issues during operation.

---

## 12. IP Restriction

By default, IP restriction is disabled for development:

```env
ENABLE_IP_RESTRICTION=False
```

For clinic network deployment, it can be enabled:

```env
ENABLE_IP_RESTRICTION=True
```

Allowed IP prefixes can be adjusted:

```env
ALLOWED_IP_PREFIXES=127.,192.168.,10.
```

Explanation:

- `127.` allows localhost access.
- `192.168.` allows common WiFi or LAN network access.
- `10.` allows private network access.

If IP restriction is enabled, only devices with allowed IP prefixes can access the system.

---

## 13. Database Location

The system uses SQLite database.

The database file is stored in:

```text
instance/clinic.sqlite
```

This file contains operational data such as:

- Users
- Patients
- Queue data
- Visit records
- Prescriptions
- Medicine inventory
- Audit logs

The database file should not be uploaded to GitHub.

---

## 14. Database Backup

To backup the database, run:

```text
backup_database.bat
```

The backup file will be saved in:

```text
backups/
```

Backup file example:

```text
clinic_backup_20260714_153000.sqlite
```

It is recommended to backup the database regularly, especially before updating the application.

The `backups/` folder is excluded from Git using `.gitignore`.

---

## 15. Demo Data

The system provides demo data seeder files:

```text
seed_demo_data.py
seed_demo_data.bat
```

To create demo data, run:

```bash
python seed_demo_data.py
```

Or double-click:

```text
seed_demo_data.bat
```

The demo data includes:

- Admin account
- Doctor account
- Receptionist account
- Sample patients
- Sample medicines
- Sample queue records
- Sample visit and prescription records
- Sample audit log records

This is useful for presentation and system demonstration.

---

## 16. Default Login Accounts

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

## 17. Security Notes for Deployment

Before production deployment:

- Change the default `SECRET_KEY`.
- Use strong passwords for all users.
- Change default account passwords.
- Enable IP restriction if the system is only used inside clinic network.
- Set `SESSION_COOKIE_SECURE=True` when using HTTPS.
- Backup the database regularly.
- Do not upload `.env` file to GitHub.
- Do not upload database files to GitHub.
- Do not upload log files to GitHub.
- Limit access to the server computer.
- Keep dependencies updated.

---

## 18. Testing Before Deployment

Before deployment, run automated tests:

```bash
pytest
```

Expected final result:

```text
18 passed, 0 warnings
```

Manual checks before deployment:

1. Login as Admin.
2. Login as Doctor.
3. Login as Receptionist.
4. Add patient.
5. Edit patient.
6. Create queue.
7. Call patient as Doctor.
8. Save examination.
9. Add prescription.
10. Check medicine stock reduction.
11. Open medical record.
12. Print medical record.
13. Export patient data.
14. Export inventory.
15. Export audit log.
16. Open health check endpoint.
17. Check production log file.
18. Backup database.

---

## 19. Running Summary

For a new computer, the complete setup flow is:

```bash
git clone https://github.com/terimakasihya555/clinic-management-system.git
cd clinic-management-system
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
copy .env.example .env
python run.py
```

For production mode:

```bash
python serve.py
```

Then open:

```text
http://127.0.0.1:5000
```

For health check:

```text
http://127.0.0.1:5000/health/
```

---

## 20. Troubleshooting

### Problem: `ModuleNotFoundError`

If an error appears such as:

```text
ModuleNotFoundError: No module named 'flask_login'
```

Solution:

```bash
venv\Scripts\activate.bat
pip install -r requirements.txt
python run.py
```

---

### Problem: `ModuleNotFoundError: No module named 'dotenv'`

Solution:

```bash
venv\Scripts\activate.bat
pip install python-dotenv
pip install -r requirements.txt
```

Make sure `python-dotenv` is included in `requirements.txt`.

---

### Problem: Application cannot be accessed from another device

Check the following:

- Both devices are connected to the same WiFi or LAN.
- The server computer firewall allows port 5000.
- The correct IPv4 address is used.
- The application is running using `serve.py` with host `0.0.0.0`.

---

### Problem: Database not found

Make sure the application has been run at least once.

The SQLite database will be created automatically in the `instance` folder.

---

### Problem: 403 Forbidden

This may happen if:

- The user role does not have access to the page.
- IP restriction is enabled and the device IP is not allowed.

Check:

```env
ENABLE_IP_RESTRICTION
ALLOWED_IP_PREFIXES
```

---

### Problem: Log file becomes too large

The system uses rotating log files. If needed, old log files can be archived or deleted manually.

Log files are stored in:

```text
logs/
```

---

## 21. Deployment Conclusion

The Clinic Management System can be deployed locally on one computer or accessed by multiple devices in the same clinic network.

The system supports production serving through Waitress, configurable environment variables, IP restriction, database backup, health check endpoint, production logging, and role-based access control.

This deployment approach is suitable for small clinic environments that require a lightweight, local-network-based web application.