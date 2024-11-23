from django.shortcuts import render, redirect
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def sign_up(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully")

            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'users/signup.html', context)

def login_user(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('post_home')
        else:
            messages.error(request, "Invalid username or password.")

    context = {
        'form': form
    }
    return render(request, 'users/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('post_home')

