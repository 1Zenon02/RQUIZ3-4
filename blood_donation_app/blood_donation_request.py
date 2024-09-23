# blood_donation_models.py
from django.db import models

class BloodDonationRequest(models.Model):
    # define the fields for the Blood Donation Request model
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=10)
    # add other fields as needed