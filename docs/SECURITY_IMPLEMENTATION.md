# Security Implementation

This document describes the security mechanisms implemented in the Clinic Management System.

## 1. Authentication

The system requires users to login before accessing protected pages. Flask-Login is used to manage user sessions.

## 2. Password Hashing

User passwords are not stored in plain text. Passwords are stored using hashing through Werkzeug security functions.

## 3. Role-Based Access Control

The system uses role-based access control to restrict access based on user responsibilities.

Available roles:
- Admin
- Doctor
- Receptionist

Each route is protected using a role guard function. Unauthorized users receive a 403 Forbidden response.

## 4. Session Timeout

The system records user activity time in session data. If the session is inactive for a configured period, the user is logged out automatically.

## 5. Security Headers

The system applies several HTTP security headers:
- `X-Content-Type-Options`
- `X-Frame-Options`
- `Referrer-Policy`
- `Permissions-Policy`

These headers help reduce common web security risks.

## 6. IP Restriction Configuration

The system provides configurable IP restriction. This feature can be enabled during deployment to limit access only from the clinic network.

## 7. Simple Rate Limiting

The system includes simple request rate limiting based on client IP address. This helps reduce excessive request attempts.

## 8. Audit Logging

The system records data-changing activities, including POST, PUT, PATCH, and DELETE requests. Each log stores:
- User ID
- Action
- Module
- IP address
- User agent
- Timestamp

## 9. Anti-Copy Script

The system includes a client-side anti-copy script to reduce casual copying of sensitive data. This is not treated as full security protection, but as an additional deterrent.

## 10. Error Handling

The system provides custom error pages for:
- 403 Forbidden
- 404 Not Found
- 500 Internal Server Error

This improves user experience and avoids exposing unnecessary technical details.

## Summary

The security design combines authentication, authorization, session management, audit logging, security headers, and configurable network restriction. These controls support safer access to clinic data and improve system accountability.