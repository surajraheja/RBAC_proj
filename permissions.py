from .models import User

def validate_access(user_id, resource, action):
    try:
        user = User.objects.get(id=user_id)
        role_permissions = user.permissions.filter(resource=resource, action=action)

        if role_permissions.exists():
            return True
        return False
    except User.DoesNotExist:
        return False
