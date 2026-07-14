# Test Cases

This document summarizes functional testing performed on the Clinic Management System.

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
| 11 | Create queue | Receptionist creates walk-in queue | Queue number is generated | Passed |
| 12 | Emergency queue priority | Create emergency queue | Emergency appears before lower priority queues | Passed |
| 13 | Queue monitor display | Open `/queue/display` | Queue monitor is displayed | Passed |
| 14 | Doctor calls patient | Doctor clicks call patient | Queue status changes to serving | Passed |
| 15 | Save examination | Doctor inputs diagnosis and notes | Visit record is saved | Passed |
| 16 | Create prescription | Doctor inputs medicine quantity | Prescription is saved | Passed |
| 17 | Automatic stock reduction | Save prescription with medicine | Medicine stock decreases automatically | Passed |
| 18 | Insufficient stock validation | Enter quantity greater than stock | System rejects prescription | Passed |
| 19 | Stock opname in | Add stock from inventory page | Medicine stock increases | Passed |
| 20 | Stock opname out | Reduce stock from inventory page | Medicine stock decreases | Passed |
| 21 | Medical record history | Open patient medical record | Visit and prescription history are displayed | Passed |
| 22 | Audit log | Perform POST action | Activity is recorded in audit log | Passed |
| 23 | 404 page | Open invalid route | Custom 404 page is displayed | Passed |
| 24 | Security headers | Open login page | Security headers are included in response | Passed |

## Automated Testing

Automated tests are implemented using Pytest. The current test result:

```text
11 passed