# Role-Based Access Control (RBAC) System
A backend application implementing a custom Role-Based Access Control (RBAC) system to manage user roles and permissions dynamically.
This project demonstrates the design, implementation, and validation of a scalable backend solution.

# Features
*User Management: Create users and assign predefined roles (Staff, Supervisor, Admin).

*Role Management: Retrieve roles and dynamically assign permissions (Admin-only).

*Permission Management: Define and associate permissions with resources and actions.

*Access Validation: Validate user permissions for specific actions on resources.

# API Endpoints
*User Management:
POST /users: Create a new user.
GET /users: Retrieve a list of users.
POST /users/assign-role: Assign a role to a user.

*Role Management:
GET /roles: List predefined roles.
POST /roles/assign-permissions: Assign permissions to a role.

*Permission Management:
GET /permissions: List all permissions.
GET /roles/:role_id/permissions: List permissions assigned to a specific role.

*Access Validation:
POST /validate-access: Check if a user can perform an action on a resource.

# Setup Instructions
*Install Dependencies
pip install -r requirements.txt

*Set Up the Database
Configure your preferred database in the settings.py file.
Apply migrations:
python manage.py migrate

*Run the Application
python manage.py runserver

# Resources
Python Django Documentation- https://www.djangoproject.com/

Postman Documentation- https://learning.postman.com/docs/publishing-your-api/documenting-your-api/


