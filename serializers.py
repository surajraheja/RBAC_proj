from rest_framework import serializers
from .models import User, Role, Permission

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']

class UserSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())  # Reference Role by ID

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
    
    def create(self, validated_data):
        # Extract the role
        role = validated_data.pop('role', None)

        if not role:
            raise serializers.ValidationError({"role": "This field is required."})
        
        # Create the user and assign the role
        user = User.objects.create(**validated_data, role=role)
        return user

class PermissionSerializer(serializers.ModelSerializer):
    roles = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True)

    class Meta:
        model = Permission
        fields = ['id', 'name', 'resource', 'action', 'roles']

    def create(self, validated_data):
        roles_data = validated_data.pop('roles')
        permission = Permission.objects.create(**validated_data)
        permission.roles.set(roles_data)  # Associate roles
        permission.save()
        return permission
