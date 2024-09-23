# blood_donation_app/forms.py
from django import forms
from .models import User, Profile, BloodDonationRequest  # Import models used in forms

# Registration Form
class RegistrationForm(forms.ModelForm):
    """
    Form for user registration.
    """
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=255, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')

# Login Form
class LoginForm(forms.Form):
    """
    Form for user login.
    """
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255, widget=forms.PasswordInput)

# Profile Form
class ProfileForm(forms.ModelForm):
    """
    Form for creating a new profile.
    """
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'blood_type', 'availability')

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight < 0:
            self.add_error('weight', 'Weight cannot be negative')
        return weight

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height is not None and height < 0:
            self.add_error('height', 'Height cannot be negative')
        return height

# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating an existing profile.
    """
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'blood_type', 'availability')

    def clean_weight(self):
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight < 0:
            self.add_error('weight', 'Weight cannot be negative')
        return weight

    def clean_height(self):
        height = self.cleaned_data.get('height')
        if height is not None and height < 0:
            self.add_error('height', 'Height cannot be negative')
        return height

# Blood Donation Request Form
class BloodDonationRequestForm(forms.ModelForm):
    """
    Form for creating a blood donation request.
    """
    class Meta:
        model = BloodDonationRequest
        fields = ['request_type', 'blood_type', 'region', 'province', 'municipality']
