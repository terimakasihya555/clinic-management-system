# User Role Matrix

This document describes the access rights of each user role in the Clinic Management System.

| Module / Feature | Admin | Doctor | Receptionist |
|---|---:|---:|---:|
| Login | Yes | Yes | Yes |
| Dashboard | Yes | Yes | Yes |
| Patient List | Yes | Yes | Yes |
| Add Patient | Yes | No | Yes |
| Delete Patient | Yes | No | No |
| View Medical Record | Yes | Yes | No |
| Create Queue | Yes | No | Yes |
| View Queue | Yes | Yes | Yes |
| Call Patient | Yes | Yes | No |
| Finish Queue | Yes | Yes | No |
| Cancel Queue | Yes | No | Yes |
| Doctor Examination | Yes | Yes | No |
| Create Prescription | Yes | Yes | No |
| View Inventory | Yes | No | Yes |
| Add Medicine | Yes | No | No |
| Edit Medicine | Yes | No | No |
| Delete Medicine | Yes | No | No |
| Stock Opname | Yes | No | Yes |
| Audit Log | Yes | No | No |
| User Management | Yes | No | No |
| Manage User Role | Yes | No | No |
| Queue Monitor Display | Yes | Yes | Yes |

## Explanation

The system uses Role-Based Access Control (RBAC) to limit user access based on responsibilities. Admin has full access to system management features. Doctor focuses on patient examination, medical records, and prescription. Receptionist handles patient registration, queue creation, and stock opname support.

This access separation improves data security and prevents unauthorized users from accessing sensitive medical or administrative information.