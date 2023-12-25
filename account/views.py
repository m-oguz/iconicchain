from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
# Create your views here.


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate (request, username=username, password=password )

        if user is not None:  
            login(request, user)
            return redirect("index")
        else: 
            return render(request, "account/login.html", {
                "error": "Incorrect username or password. Please try again.  "
                })
    return render(request, "account/login.html")        


def register_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]

        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", {"error": "Username already exists. Please try again."})
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html", {"error" : "E-mail address is in use"})
                else: 
                    user= User.objects.create_user(username = username, email = email, password = password, first_name = firstname, last_name = lastname)  
                    user.save()

                    return redirect("login")
        else:
            return render(request, "account/register.html", {
                "error": "Passwords do not match. Please try again."})
    else:
        return render(request, "account/register.html")

def logout_request(request):
    logout(request) 
    return redirect("index")