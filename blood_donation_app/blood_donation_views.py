# blood_donation_views.py
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BloodDonationRequest
from .forms import BloodDonationRequestForm

class BloodDonationRequestListView(ListView):
    model = BloodDonationRequest
    template_name = 'blood_donation_templates/blood_donation_request_list.html'

class BloodDonationRequestCreateView(CreateView):
    model = BloodDonationRequest
    form_class = BloodDonationRequestForm
    template_name = 'blood_donation_templates/blood_donation_request_create.html'
    success_url = '/blood-donation-requests/'

class BloodDonationRequestUpdateView(UpdateView):
    model = BloodDonationRequest
    form_class = BloodDonationRequestForm
    template_name = 'blood_donation_templates/blood_donation_request_update.html'
    success_url = '/blood-donation-requests/'

class BloodDonationRequestDeleteView(DeleteView):
    model = BloodDonationRequest
    template_name = 'blood_donation_templates/blood_donation_request_delete.html'
    success_url = '/blood-donation-requests/'