# Permissions and Groups Setup

This project implements Role-Based Access Control (RBAC) using Django permissions and groups.

## Custom Permissions
Defined in the Book model:
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Enforcement
Views are protected using @permission_required decorators.

## Testing
Permissions were tested by logging in as users from each group and verifying access.
403 Forbidden responses confirm correct enforcement.
