from rest_framework import viewsets
from .models import User, Role, Permission
from .serializers import UserSerializer, RoleSerializer, PermissionSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import validate_access
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(APIView):
    def delete(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            user.delete()
            return Response({"message": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDeleteView(APIView):
    def delete(self, request, pk):
        try:
            role = Role.objects.get(pk=pk)
            role.delete()  # This cascades to delete all associated users
            return Response({"message": "Role and its users deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Role.DoesNotExist:
            return Response({"error": "Role not found."}, status=status.HTTP_404_NOT_FOUND)

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer

    # Example of custom endpoint to add permissions to roles
    @action(detail=False, methods=['post'])
    def assign_permissions(self, request):
        permission_data = request.data
        role_ids = permission_data.pop('role_ids', [])
        permission = Permission.objects.create(**permission_data)
        if role_ids:
            roles = Role.objects.filter(id__in=role_ids)
            permission.roles.set(roles)
            permission.save()
        return Response(permission_data, status=201)
    
class PermissionDeleteView(APIView):
    def delete(self, request, pk):
        try:
            permission = Permission.objects.get(pk=pk)
            permission.delete()
            return Response({"message": "Permission deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        except Permission.DoesNotExist:
            return Response({"error": "Permission not found."}, status=status.HTTP_404_NOT_FOUND)

class AccessValidationView(APIView):
    def post(self, request):
        username = request.data.get("username")
        resource = request.data.get("resource")
        action = request.data.get("action")

        # Check if all required fields are provided
        if not username or not resource or not action:
            return Response({"error": "username, resource, and action are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Get the user and their role
        try:
            user = User.objects.select_related("role").get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Get the permissions for the user's role
        role_permissions = Permission.objects.filter(role=user.role, resource=resource, action=action)

        if role_permissions.exists():
            return Response({"message": "Access granted."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Access denied."}, status=status.HTTP_403_FORBIDDEN)