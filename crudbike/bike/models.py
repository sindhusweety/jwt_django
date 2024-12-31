from django.db import models
from django.contrib.auth.models import AbstractUser

# Custom User Model (if needed)
class User(AbstractUser):
    pass

# Bike Model
class Bike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bikes")
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    purchase_date = models.DateField()

    def __str__(self):
        return self.name



