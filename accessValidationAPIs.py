from .views import AccessValidationView
from django.http import JsonResponse  # Import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Permission, Role  # Import the Permission and Role models
from rest_framework import status  # Import the status module

class APIOneView(APIView):
    def get(self, request, *args, **kwargs):
        role_name = request.query_params.get('role', None)
        
        if not role_name:
            return JsonResponse({
                "success": False,
                "message": "Role parameter is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fetch the role object
            role = Role.objects.get(name=role_name)
        except Role.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": f"Role '{role_name}' does not exist"
            }, status=status.HTTP_404_NOT_FOUND)
        
        if role_name.lower() == "admin":
            return JsonResponse({
                "success": True,
                "message": "Access granted",
                "data": "Relevant data for API_ONE"
            }, status=status.HTTP_200_OK)


        # Check if the role has access to API_ONE
        permission = Permission.objects.filter(resource="API_ONE", action="Access", roles=role).exists()
        
        if permission:
            return JsonResponse({
                "success": True,
                "message": "Access granted",
                "data": "Relevant data for API_ONE"
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                "success": False,
                "message": f"Role '{role_name}' does not have permission to access 'Api_one'"
            }, status=status.HTTP_403_FORBIDDEN)


class APITwoView(APIView):
    def get(self, request, *args, **kwargs):
        role_name = request.query_params.get('role', None)
        
        if not role_name:
            return JsonResponse({
                "success": False,
                "message": "Role parameter is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fetch the role object
            role = Role.objects.get(name=role_name)
        except Role.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": f"Role '{role_name}' does not exist"
            }, status=status.HTTP_404_NOT_FOUND)
        
        if role_name.lower() == "admin":
            return JsonResponse({
                "success": True,
                "message": "Access granted",
                "data": "Relevant data for API_TWO"
            }, status=status.HTTP_200_OK)
        
        # Check if the role has access to API_TWO
        permission = Permission.objects.filter(resource="API_TWO", action="Access", roles=role).exists()
        
        if permission:
            return JsonResponse({
                "success": True,
                "message": "Access granted",
                "data": "Relevant data for API_TWO"
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                "success": False,
                "message": f"Role '{role_name}' does not have permission to access 'Api_two'"
            }, status=status.HTTP_403_FORBIDDEN)


class APIThreeView(APIView):
    def get(self, request, *args, **kwargs):
        role_name = request.query_params.get('role', None)
        
        if not role_name:
            return JsonResponse({
                "success": False,
                "message": "Role parameter is required"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            # Fetch the role object
            role = Role.objects.get(name=role_name)
        except Role.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": f"Role '{role_name}' does not exist"
            }, status=status.HTTP_404_NOT_FOUND)
        
        if role_name.lower() == "admin":
            return JsonResponse({
                "success": True,
                "message": "Access granted",
                "data": "Relevant data for API_THREE"
            }, status=status.HTTP_200_OK)
        
        # Check if the role has access to API_THREE
        permission = Permission.objects.filter(resource="API_THREE", action="Access", roles=role).exists()
        
        if permission:
            return JsonResponse({
                "success": True,
                "message": "Access granted",
                "data": "Relevant data for API_THREE"
            }, status=status.HTTP_200_OK)
        else:
            return JsonResponse({
                "success": False,
                "message": f"Role '{role_name}' does not have permission to access 'Api_three'"
            }, status=status.HTTP_403_FORBIDDEN)