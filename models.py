from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    roles = models.ManyToManyField(Role, related_name='permissions')

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="users"
    )  # Cascade delete users when a role is deleted

    def __str__(self):
        return self.username
