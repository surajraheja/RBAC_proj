from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from .accessValidationAPIs import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
    path('roles/<int:pk>/', RoleDeleteView.as_view(), name='delete-role'),
    path('permissions/<int:pk>/', PermissionDeleteView.as_view(), name='delete-permission'),
    path('api_one/', APIOneView.as_view(), name='api_one'),
    path('api_two/', APITwoView.as_view(), name='api_two'),
    path('api_three/', APIThreeView.as_view(), name='api_three'),
    path("validate_access/", AccessValidationView.as_view(), name="validate_access"),
]
