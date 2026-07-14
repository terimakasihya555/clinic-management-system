# Testing and Evaluation Summary

## 1. Testing Overview

Testing was conducted to ensure that the Clinic Management System works according to its functional requirements. The testing process includes manual testing and automated testing using Pytest.

Manual testing was performed by running the application and testing each module through the browser. Automated testing was performed to check important routes, authentication, role access, and security headers.

## 2. Testing Objectives

The objectives of testing are:

1. To ensure the login system works correctly.
2. To ensure protected pages cannot be accessed without login.
3. To ensure role-based access control works correctly.
4. To ensure main pages can be opened.
5. To ensure error pages are displayed correctly.
6. To ensure security headers are included in responses.
7. To ensure the queue display page is accessible.
8. To ensure admin can access user management.
9. To ensure doctor cannot access admin-only pages.

## 3. Automated Testing Tool

The automated tests use:

```text
Pytest
```

Test files are stored in:

```text
tests/
```

Test files:

| File | Description |
|---|---|
| `test_basic.py` | Tests basic pages and public routes. |
| `test_auth.py` | Tests login and role access. |
| `test_security.py` | Tests security headers and protected routes. |
| `conftest.py` | Provides test configuration. |

## 4. Automated Testing Result

The latest automated test result is:

```text
11 passed
```

This means all automated tests passed successfully.

## 5. Automated Test Coverage

The automated tests cover:

| No | Test Area | Description | Result |
|---:|---|---|---|
| 1 | Login Page | Login page can be opened | Passed |
| 2 | Dashboard Protection | Dashboard redirects user if not logged in | Passed |
| 3 | 404 Page | Invalid route returns 404 | Passed |
| 4 | Queue Display | Queue monitor page can be opened | Passed |
| 5 | Admin Login | Admin can login successfully | Passed |
| 6 | Invalid Login | Wrong password is rejected | Passed |
| 7 | Doctor Restriction | Doctor cannot access user management | Passed |
| 8 | Admin Access | Admin can access user management | Passed |
| 9 | Security Headers | Security headers are included | Passed |
| 10 | Unauthenticated Redirect | Unauthenticated user is redirected to login | Passed |
| 11 | Custom Error Page | Custom error page response works | Passed |

## 6. Manual Testing Summary

Manual testing was also performed for the main system workflow.

| No | Scenario | Expected Result | Status |
|---:|---|---|---|
| 1 | Add patient | Patient data is saved | Passed |
| 2 | Search patient | Matching patient is displayed | Passed |
| 3 | Create queue | Queue number is generated | Passed |
| 4 | Emergency queue priority | Emergency appears first | Passed |
| 5 | Doctor calls patient | Queue status changes to serving | Passed |
| 6 | Save examination | Visit record is saved | Passed |
| 7 | Add prescription | Prescription is saved | Passed |
| 8 | Stock reduction | Medicine stock decreases | Passed |
| 9 | Insufficient stock | System rejects prescription | Passed |
| 10 | Stock opname in | Medicine stock increases | Passed |
| 11 | Stock opname out | Medicine stock decreases | Passed |
| 12 | Medical record history | Visit history is displayed | Passed |
| 13 | Audit log | User activity is recorded | Passed |
| 14 | Add user | User account is created | Passed |
| 15 | Change user role | User role is updated | Passed |
| 16 | Prevent self role change | Active admin role cannot be changed | Passed |

## 7. Evaluation Result

Based on the testing result, the system successfully performs the main clinic operational functions. The system can manage patient data, queue priority, doctor examination, prescription, medicine stock, medical record history, audit log, and user access control.

The automated testing result shows that important system routes and access restrictions work correctly. Manual testing also confirms that the main workflow can be completed from patient registration to examination and medical record storage.

## 8. Limitation of Testing

The current testing focuses on functional testing and basic security route testing. More advanced testing can be added in the future, such as:

- Load testing
- Browser compatibility testing
- Database migration testing
- API testing
- End-to-end testing
- Security penetration testing

## 9. Conclusion

Testing results show that the Clinic Management System works according to the expected functionality. The system passed automated tests and manual workflow tests. Therefore, the system is ready for final demonstration and thesis evaluation.