from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Login now!")
            return redirect('user-login')
    else:
        if request.user.is_authenticated:
            return redirect('shop-home')
        else:
            form = UserRegisterForm()
    return render(request, 'users/register.html', {'title':"Register", 'form':form})

@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('user-login')