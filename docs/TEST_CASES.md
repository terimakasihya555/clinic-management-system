# Test Cases

This document summarizes functional testing and automated testing performed on the Clinic Management System.

---

## 1. Manual Test Cases

| No | Test Scenario | Test Steps | Expected Result | Status |
|---:|---|---|---|---|
| 1 | Login page loads | Open `/auth/login` | Login page is displayed | Passed |
| 2 | Admin login | Login using admin account | Admin dashboard is displayed | Passed |
| 3 | Doctor login | Login using doctor account | Doctor dashboard is displayed | Passed |
| 4 | Receptionist login | Login using receptionist account | Receptionist dashboard is displayed | Passed |
| 5 | Invalid login | Enter wrong password | System rejects login | Passed |
| 6 | Dashboard protection | Open `/dashboard` without login | User is redirected to login page | Passed |
| 7 | Doctor access restriction | Doctor opens `/users/` | System displays 403 page | Passed |
| 8 | Admin access user management | Admin opens `/users/` | User Management page is displayed | Passed |
| 9 | Add patient | Receptionist creates patient | Patient data is saved | Passed |
| 10 | Search patient | Search patient by name | Matching patient data is displayed | Passed |
| 11 | Edit patient | Admin or Receptionist updates patient data | Patient data is updated | Passed |
| 12 | Doctor cannot edit patient | Doctor tries to update patient data | System returns 403 Forbidden | Passed |
| 13 | Create queue | Receptionist creates walk-in queue | Queue number is generated | Passed |
| 14 | Emergency queue priority | Create emergency queue | Emergency appears before lower priority queues | Passed |
| 15 | Appointment queue priority | Create appointment queue | Appointment appears before walk-in queue | Passed |
| 16 | Queue monitor display | Open `/queue/display` | Queue monitor is displayed | Passed |
| 17 | Doctor calls patient | Doctor clicks call patient | Queue status changes to serving | Passed |
| 18 | Save examination | Doctor inputs diagnosis and notes | Visit record is saved | Passed |
| 19 | Create prescription | Doctor inputs medicine quantity | Prescription is saved | Passed |
| 20 | Automatic stock reduction | Save prescription with medicine | Medicine stock decreases automatically | Passed |
| 21 | Insufficient stock validation | Enter quantity greater than stock | System rejects prescription | Passed |
| 22 | Stock opname in | Add stock from inventory page | Medicine stock increases | Passed |
| 23 | Stock opname out | Reduce stock from inventory page | Medicine stock decreases | Passed |
| 24 | Medical record history | Open patient medical record | Visit and prescription history are displayed | Passed |
| 25 | Print medical record | Click print button on medical record page | Print dialog is opened | Passed |
| 26 | Export patient data | Click Export Excel on patient page | Excel file is downloaded | Passed |
| 27 | Export medical record | Click Export Excel on medical record page | Excel file is downloaded | Passed |
| 28 | Export inventory | Click Export Excel on inventory page | Excel file is downloaded | Passed |
| 29 | Export audit log | Click Export Excel on audit page | Excel file is downloaded | Passed |
| 30 | Audit log | Perform POST action | Activity is recorded in audit log | Passed |
| 31 | 404 page | Open invalid route | Custom 404 page is displayed | Passed |
| 32 | 403 page | Access unauthorized page | Custom 403 page is displayed | Passed |
| 33 | Security headers | Open login page | Security headers are included in response | Passed |
| 34 | Health check endpoint | Open `/health/` | JSON health status is returned | Passed |
| 35 | Production logging | Run application | Log file is created in `logs/` | Passed |
| 36 | Database backup | Run `backup_database.bat` | Backup file is created | Passed |

---

## 2. Automated Testing

Automated tests are implemented using Pytest.

Run the tests:

```bash
pytest
```

Final automated test result:

```text
18 passed, 0 warnings
```

---

## 3. Automated Test Coverage

The automated tests cover:

| No | Test Area | Description | Status |
|---:|---|---|---|
| 1 | Login page | Checks whether login page can be accessed | Passed |
| 2 | Admin login | Checks successful admin login | Passed |
| 3 | Invalid login | Checks invalid login rejection | Passed |
| 4 | Dashboard protection | Checks unauthenticated dashboard access | Passed |
| 5 | User role restriction | Checks unauthorized role access | Passed |
| 6 | User management access | Checks admin access to user management | Passed |
| 7 | Queue display | Checks public queue display page | Passed |
| 8 | 404 page | Checks custom not found page | Passed |
| 9 | Security headers | Checks security headers in response | Passed |
| 10 | Patient update | Checks whether admin can update patient data | Passed |
| 11 | Doctor patient update restriction | Checks doctor cannot update patient data | Passed |
| 12 | Patient Excel export | Checks patient export returns Excel file | Passed |
| 13 | Medical record Excel export | Checks medical record export returns Excel file | Passed |
| 14 | Inventory Excel export | Checks inventory export returns Excel file | Passed |
| 15 | Audit log Excel export | Checks audit export returns Excel file | Passed |
| 16 | Health check endpoint | Checks health endpoint returns OK status | Passed |

---

## 4. Excel Export Test Validation

The Excel export tests validate that:

- Response status code is `200`.
- Response content type is Excel MIME type.
- Response data starts with `PK`, which indicates a valid `.xlsx` file format.

The tested export features are:

- Patient data export.
- Medical record export.
- Inventory export.
- Audit log export.

---

## 5. Security Test Validation

The security tests validate that:

- Protected pages require authentication.
- Unauthorized roles receive forbidden access.
- Security headers are included in the HTTP response.
- Invalid routes return the custom 404 page.

Security headers tested include:

- `X-Content-Type-Options`
- `X-Frame-Options`
- `Referrer-Policy`
- `Permissions-Policy`

---

## 6. Health Check Test Validation

The health check test validates the endpoint:

```text
/health/
```

Expected response:

```json
{
  "app": "Clinic Management System",
  "database": "connected",
  "status": "ok",
  "version": "1.0.0"
}
```

This confirms that:

- The application is running.
- The database connection is available.
- The application configuration can be loaded.

---

## 7. Warning Cleanup Result

During testing, deprecated warnings were cleaned from the application code.

The cleanup included:

- Replacing deprecated `datetime.utcnow()` usage.
- Using timezone-aware UTC datetime.
- Replacing legacy `Query.get()` usage where necessary.
- Preventing duplicate production log handlers.

Final test result:

```text
18 passed, 0 warnings
```

---

## 8. Testing Conclusion

The testing result shows that the main features of the Clinic Management System are working properly.

The system has passed functional testing and automated testing for authentication, access control, queue display, security headers, patient update, Excel export, health check endpoint, and error handling.

The final result of `18 passed, 0 warnings` indicates that the system is stable and ready for final demonstration, thesis evaluation, and portfolio presentation.