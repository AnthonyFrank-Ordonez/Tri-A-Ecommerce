from django.shortcuts import render, redirect
from .forms import UserRegister

from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from .models import User

# User = settings.AUTH_USER_MODEL

def register_user(request):
    """Register View for the creation of user accounts"""

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Hey {username}, your account was created successfully')
            new_user = authenticate(username=form.cleaned_data.get('email'),
                                    password=form.cleaned_data.get('password1')
            )

            login(request, new_user)
            return redirect('core:index')

    else:
        form = UserRegister()
    
    context = {
        'form': form,
    }

    return render(request, 'userauths/sign-up.html', context)


def login_user(request):
    """Login View for authenticating/logging in user accounts"""

    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('core:index')
        
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                messages.success(request, 'You are now logged in')

                return redirect('core:index')
            else:
                messages.warning(request, 'User does not exist, Create an account')

        except:
            messages.warning(request, f"User with {email} does not exist")


    return render(request, 'userauths/sign-in.html')


def logout_user(request):
    """Logout View for the logout function"""
    
    logout(request)
    messages.success(request, 'You Logged out')
    return redirect('userauths:sign-in')