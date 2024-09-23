# blood_donation_app/views.py
from django.shortcuts import render, redirect
from django.views    import View
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm, LoginForm, ProfileForm, ProfileUpdateForm



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if hasattr(user, 'profile'):
                    return redirect('homepage')
                else:
                    return redirect('create_profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('homepage')
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

class ProfileUpdateView(View):
    def get(self, request):
        form = ProfileUpdateForm(instance=request.user.profile)
        return render(request, 'update_profile.html', {'form': form})

    def post(self, request):
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            if profile.availability and profile.last_donation_date:
                days_since_last_donation = (datetime.date.today() - profile.last_donation_date).days
                if days_since_last_donation < 56:
                    form.add_error('availability', 'You need to wait {} days before you can donate blood again.'.format(56 - days_since_last_donation))
                    return render(request, 'update_profile.html', {'form': form})
            profile.save()
            return redirect('profile')
        return render(request, 'update_profile.html', {'form': form})