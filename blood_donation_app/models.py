from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    # Add related_name to resolve clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Customize the related_name to avoid conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Customize the related_name to avoid conflict
        blank=True
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    region = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=10)
    availability = models.BooleanField(default=False)
    last_donation_date = models.DateField(null=True, blank=True)

class BloodDonationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=10)
    region = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    municipality = models.CharField(max_length=255)
