from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import (
    LoginForm,
    RegisterForm
)

def logout_view(request):
    logout(request)
    return redirect("/login")

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        #verify valid username and password
        user = authenticate(username=username, password=password)
        if user == None:
            #later add message 
            return redirect("/login")
        #perform login
        login(request, user)
        #redirect
        return redirect("/")
    return render(request, "accounts/login.html",{"form":form})

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save(commit=False)
        password = form.cleaned_data.get("password")
        user_obj.save()
        user_obj.set_password(password)
        user_obj.save()
        return redirect("/login")
    return render(request, "accounts/register.html", {"form": form})