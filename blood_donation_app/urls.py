from django.urls import path
from . import views
from . import blood_donation_views

urlpatterns = [
    path('blood-donation-requests/', blood_donation_views.BloodDonationRequestListView.as_view(), name='blood_donation_request_list'),
    path('blood-donation-requests/create/', blood_donation_views.BloodDonationRequestCreateView.as_view(), name='blood_donation_request_create'),
    path('blood-donation-requests/<int:pk>/update/', blood_donation_views.BloodDonationRequestUpdateView.as_view(), name='blood_donation_request_update'),
    path('blood-donation-requests/<int:pk>/delete/', blood_donation_views.BloodDonationRequestDeleteView.as_view(), name='blood_donation_request_delete'),
]