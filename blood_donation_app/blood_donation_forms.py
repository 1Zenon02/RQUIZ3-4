# blood_donation_forms.py
from django import forms
from .models import BloodDonationRequest

class BloodDonationRequestForm(forms.ModelForm):
    class Meta:
        model = BloodDonationRequest
        fields = ('name', 'email', 'phone_number', 'blood_type')