# MVC Architecture Explanation

## 1. Overview

The Clinic Management System applies the MVC architectural concept to organize the application structure. MVC stands for Model, View, and Controller.

This structure separates database logic, user interface, and application logic into different parts. As a result, the system becomes easier to understand, maintain, and develop.

## 2. Model

The Model represents the database structure and business data.

In this system, models are implemented using SQLAlchemy and stored inside:

```text
clinic_app/models/
```

Examples of model files:

| Model | Description |
|---|---|
| User | Stores user account, email, password hash, and role. |
| Patient | Stores patient data and medical record number. |
| QueueEntry | Stores queue number, type, priority, and status. |
| Visit | Stores doctor examination result. |
| Medicine | Stores medicine data and stock. |
| Prescription | Stores prescription data linked to visit. |
| PrescriptionItem | Stores medicine items and quantity in prescription. |
| AuditLog | Stores user activity records. |

The Model layer communicates with the database through SQLAlchemy.

## 3. View

The View is responsible for displaying data to the user.

In this system, views are implemented using Jinja2 templates and Bootstrap. The templates are stored inside:

```text
clinic_app/templates/
```

Examples of view pages:

| View | Function |
|---|---|
| Login page | Displays login form. |
| Dashboard | Displays system summary. |
| Patient list | Displays patient data. |
| Queue list | Displays queue data. |
| Queue monitor | Displays queue screen for clinic monitor. |
| Doctor examination form | Displays diagnosis and prescription form. |
| Inventory page | Displays medicine stock. |
| Medical record page | Displays patient visit history. |
| Audit log page | Displays user activities. |
| User management page | Displays user accounts. |

The View layer does not directly manage database logic. It only displays data passed from the Controller.

## 4. Controller

The Controller handles user requests, processes logic, and returns responses.

In this system, controllers are implemented using Flask routes and Blueprints. They are stored inside:

```text
clinic_app/blueprints/
```

Main blueprints:

| Blueprint | Function |
|---|---|
| auth | Handles login and logout. |
| patients | Handles patient data and medical record. |
| queue | Handles queue creation and display. |
| doctor | Handles doctor examination and prescription. |
| inventory | Handles medicine inventory and stock opname. |
| audit | Handles audit log display. |
| users | Handles user management. |

The Controller receives requests from the user, interacts with the Model, and sends data to the View.

## 5. MVC Flow Example

Example: Doctor saves examination and prescription.

1. Doctor opens examination form.
2. Browser sends request to doctor route.
3. Controller receives diagnosis, notes, and prescription data.
4. Controller checks medicine stock using Medicine model.
5. Controller saves Visit, Prescription, and PrescriptionItem data.
6. Controller reduces medicine stock.
7. Controller redirects user to doctor dashboard.
8. View displays success message.

Flow:

```text
User Request → Controller → Model → Database → Controller → View → User Response
```

## 6. Benefits of MVC in This System

The MVC structure provides several benefits:

1. Clear separation of responsibilities.
2. Easier maintenance.
3. Easier testing.
4. Easier module development.
5. Better code organization.
6. Easier debugging.
7. Supports scalability for future improvements.

## 7. Conclusion

The Clinic Management System applies MVC by separating database models, user interface templates, and controller routes. This structure supports maintainability and makes the system easier to develop and explain in the thesis.