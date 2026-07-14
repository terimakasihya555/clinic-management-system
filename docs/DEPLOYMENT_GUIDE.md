# Deployment Guide

This document explains how to prepare and run the Clinic Management System on another computer or clinic environment.

## 1. Requirements

The target computer should have:

- Python installed
- Git installed
- Internet connection for initial dependency installation
- Web browser
- Local network connection if the system will be accessed by multiple devices

## 2. Clone Repository

Open Command Prompt and run:

```bash
git clone <repository-url>
cd clinic-management-system
```

Example:

```bash
git clone https://github.com/terimakasihya555/clinic-management-system.git
cd clinic-management-system
```

## 3. Create Virtual Environment

Create a virtual environment:

```bash
python -m venv venv
```

## 4. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate.bat
```

After activation, the terminal should show:

```text
(venv) C:\path\to\clinic-management-system>
```

## 5. Install Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

## 6. Run in Local Development Mode

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

## 7. Run in Production Mode

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

## 8. Access from Other Devices in the Same Network

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

## 9. IP Restriction

By default, IP restriction is disabled for development:

```python
ENABLE_IP_RESTRICTION = False
```

For clinic network deployment, it can be enabled in `config.py`:

```python
ENABLE_IP_RESTRICTION = True
```

Allowed IP prefixes can be adjusted in `config.py`:

```python
ALLOWED_IP_PREFIXES = [
    "127.",
    "192.168.",
    "10."
]
```

Explanation:

- `127.` allows localhost access.
- `192.168.` allows common WiFi or LAN network access.
- `10.` allows private network access.

## 10. Database Location

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

## 11. Database Backup

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

## 12. Environment Configuration

The project includes an example environment file:

```text
.env.example
```

Example content:

```env
SECRET_KEY=change-this-secret-key
DATABASE_URL=sqlite:///clinic.sqlite
ENABLE_IP_RESTRICTION=False
SESSION_COOKIE_SECURE=False
```

For real deployment, create a `.env` file based on `.env.example` and adjust the values.

Important note:

```text
Do not upload the real .env file to GitHub.
```

## 13. Security Notes for Deployment

Before production deployment:

- Change the default `SECRET_KEY`.
- Use strong passwords for all users.
- Change default account passwords.
- Enable IP restriction if the system is only used inside clinic network.
- Set `SESSION_COOKIE_SECURE = True` when using HTTPS.
- Backup the database regularly.
- Do not upload `.env` file to GitHub.
- Do not share the database file publicly.
- Limit access to the server computer.

## 14. Default Login Accounts

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

## 15. Running Summary

For a new computer, the complete setup flow is:

```bash
git clone https://github.com/terimakasihya555/clinic-management-system.git
cd clinic-management-system
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
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

## 16. Troubleshooting

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

### Problem: Application cannot be accessed from another device

Check the following:

- Both devices are connected to the same WiFi or LAN.
- The server computer firewall allows port 5000.
- The correct IPv4 address is used.
- The application is running using `serve.py` with host `0.0.0.0`.

### Problem: Database not found

Make sure the application has been run at least once. The SQLite database will be created automatically in the `instance` folder.

### Problem: 403 Forbidden

This may happen if:

- The user role does not have access to the page.
- IP restriction is enabled and the device IP is not allowed.

Check:

```python
ENABLE_IP_RESTRICTION
ALLOWED_IP_PREFIXES
```

## 17. Deployment Conclusion

The Clinic Management System can be deployed locally on one computer or accessed by multiple devices in the same clinic network. The system supports production serving through Waitress, configurable IP restriction, database backup, and role-based access control.

This deployment approach is suitable for small clinic environments that require a lightweight, local-network-based web application.