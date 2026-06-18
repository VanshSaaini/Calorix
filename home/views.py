from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .models import UserStats


def signup(request):
    # Already logged in? Go home.
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        fname        = request.POST.get('fname', '').strip()
        lname        = request.POST.get('lname', '').strip()
        email        = request.POST.get('email', '').strip()
        password     = request.POST.get('password', '')
        confirm_pass = request.POST.get('confirm_password', '')

        # Validate all fields present
        if not all([fname, lname, email, password, confirm_pass]):
            messages.error(request, "Please fill all fields!")
            return redirect('signup')

        # Passwords match
        if password != confirm_pass:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Duplicate email
        if User.objects.filter(username=email).exists():
            messages.error(request, "An account with this email already exists!")
            return redirect('signup')

        # Create user + stats
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=fname,
            last_name=lname,
        )
        UserStats.objects.create(user=user)

        messages.success(request, "Account created! Please log in.")
        return redirect('login')

    return render(request, 'home/signup.html')


def login(request):
    # Already logged in? Go home.
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email    = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        next_url = request.POST.get('next', '')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            # Honour the ?next= redirect for protected pages
            if next_url:
                return redirect(next_url)
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")

    # Pass ?next= into the template so the form can carry it forward
    next_url = request.GET.get('next', '')
    return render(request, 'home/login.html', {'next': next_url})

def logout_view(request):
    logout(request)
    return redirect('login')

#@login_required(login_url='login')
def home(request):
    return render(request, 'home/home.html')

def aboutUs(request):
    return render(request,'home/aboutUs.html')