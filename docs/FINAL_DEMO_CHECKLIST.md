# Final Demo Checklist

This checklist should be completed before presenting the Clinic Management System.

## 1. Project Preparation

| No | Checklist | Status |
|---:|---|---|
| 1 | Virtual environment is created | Done |
| 2 | Dependencies are installed | Done |
| 3 | Application can run using `python run.py` | Done |
| 4 | Application can run using `python serve.py` | Done |
| 5 | README is updated | Done |
| 6 | Documentation files are available in `docs` folder | Done |
| 7 | Tests are passing | Done |
| 8 | GitHub repository is updated | Done |
| 9 | Deployment files are available | Done |
| 10 | Backup script is available | Done |

## 2. Account Preparation

| Role | Email | Password | Status |
|---|---|---|---|
| Admin | admin@clinic.local | admin123 | Ready |
| Doctor | doctor@clinic.local | doctor123 | Ready |
| Receptionist | reception@clinic.local | reception123 | Ready |

## 3. Demo Data Preparation

| No | Data | Status |
|---:|---|---|
| 1 | At least one patient exists | Ready |
| 2 | At least one medicine exists | Ready |
| 3 | Medicine stock is sufficient | Ready |
| 4 | Queue data can be created | Ready |
| 5 | Doctor can create examination record | Ready |
| 6 | Prescription can reduce stock | Ready |
| 7 | Medical record history can be displayed | Ready |
| 8 | Audit log has activity records | Ready |
| 9 | User management contains default users | Ready |
| 10 | Queue monitor can be opened | Ready |

## 4. Demo Flow Checklist

| No | Demo Step | Status |
|---:|---|---|
| 1 | Open login page | Ready |
| 2 | Login as Admin | Ready |
| 3 | Show admin dashboard | Ready |
| 4 | Show patient data | Ready |
| 5 | Show user management | Ready |
| 6 | Show audit log | Ready |
| 7 | Logout admin | Ready |
| 8 | Login as Receptionist | Ready |
| 9 | Add patient | Ready |
| 10 | Create queue | Ready |
| 11 | Open queue list | Ready |
| 12 | Open queue monitor | Ready |
| 13 | Logout receptionist | Ready |
| 14 | Login as Doctor | Ready |
| 15 | Open doctor dashboard | Ready |
| 16 | Call patient | Ready |
| 17 | Fill diagnosis and notes | Ready |
| 18 | Add prescription | Ready |
| 19 | Save examination | Ready |
| 20 | Open medical record | Ready |
| 21 | Show stock reduction | Ready |
| 22 | Demonstrate role restriction | Ready |
| 23 | Show custom 403 page | Ready |
| 24 | Show custom 404 page | Ready |

## 5. Security Demo Checklist

| No | Security Feature | Demo Method | Status |
|---:|---|---|---|
| 1 | Login required | Open dashboard without login | Ready |
| 2 | Role restriction | Doctor opens `/users/` | Ready |
| 3 | Custom 403 page | Unauthorized access | Ready |
| 4 | Custom 404 page | Open invalid URL | Ready |
| 5 | Audit log | Perform data-changing action | Ready |
| 6 | Password hashing | Explain through code | Ready |
| 7 | Session timeout | Explain from configuration | Ready |
| 8 | IP restriction | Explain from configuration | Ready |
| 9 | Security headers | Explain from test result | Ready |
| 10 | Rate limiting | Explain from security file | Ready |

## 6. Testing Checklist

| No | Testing Item | Status |
|---:|---|---|
| 1 | Pytest can run successfully | Done |
| 2 | Login page test passed | Done |
| 3 | Dashboard protection test passed | Done |
| 4 | 404 page test passed | Done |
| 5 | Queue display test passed | Done |
| 6 | Admin login test passed | Done |
| 7 | Invalid login test passed | Done |
| 8 | Doctor role restriction test passed | Done |
| 9 | Admin access user management test passed | Done |
| 10 | Security headers test passed | Done |

Current test result:

```text
11 passed
```

## 7. Deployment Checklist

| No | Deployment Item | Status |
|---:|---|---|
| 1 | `serve.py` exists | Done |
| 2 | `start_local.bat` exists | Done |
| 3 | `start_production.bat` exists | Done |
| 4 | `backup_database.bat` exists | Done |
| 5 | `.env.example` exists | Done |
| 6 | `DEPLOYMENT_GUIDE.md` exists | Done |
| 7 | Waitress is added to requirements | Done |
| 8 | Production server can run | Done |

## 8. Final Command Checklist

Run tests:

```bash
pytest
```

Run development server:

```bash
python run.py
```

Run production server:

```bash
python serve.py
```

Backup database:

```text
backup_database.bat
```

Check Git status:

```bash
git status
```

Commit final update:

```bash
git add .
git commit -m "Add final demo and thesis support documents"
git push
```

## 9. Notes for Presentation

Important points to explain:

- The system uses Flask and SQLAlchemy.
- The system applies MVC structure.
- Queue priority is based on emergency, appointment, and walk-in.
- Prescription is connected to medicine stock.
- Medical record history stores patient examination records.
- Role-based access control protects sensitive features.
- Audit log supports accountability.
- Testing is done using Pytest.
- Deployment can be done locally or inside clinic network.

## 10. Final Demo Conclusion

Before the demo, make sure the application can run properly, default accounts can login, demo data is available, and tests are passing.

The final demo should show the complete workflow from patient registration, queue creation, doctor examination, prescription, stock reduction, medical record history, audit log, and role-based access control.