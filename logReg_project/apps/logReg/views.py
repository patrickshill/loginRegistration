from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    #save session variables
    if "first_name" not in request.session:
        request.session["first_name"]   = ""
        request.session["last_name"]    = ""
        request.session["email"]        = ""

    return render(request, "logReg/index.html")

def register(request):
    errors = User.objects.registration_validator(request.POST)

    if errors:
        #save session variables
        request.session["first_name"]   = request.POST["first_name"]
        request.session["last_name"]    = request.POST["last_name"]
        request.session["email"]        = request.POST["email"]

        #add errors to messages.error
        for key in errors:
            for msg in errors[key]:
                messages.error(request, msg, extra_tags="registration")
        return redirect("/")
    else:
        if request.method == "POST":
            first_name  = request.POST["first_name"]
            last_name   = request.POST["last_name"]
            email       = request.POST["email"]
            password    = request.POST["password"]

            #create new user
            User.objects.create(first_name=first_name, last_name=last_name,email=email,password=password)

            #store first name in session
            request.session["first_name"]   = first_name

            #success message
            messages.success(request, "Successfully registered (or logged in)!")

    return redirect("/success")

def login(request):
    errors = User.objects.login_validator(request.POST)

    if errors:
        for error in errors:
            messages.error(request, errors[error],extra_tags="login")
        return redirect("/")
    else:
        if request.method == "POST":
            user = User.objects.get(email=request.POST["email"])
            request.session["first_name"] = user.first_name
            
            #success message
            messages.success(request, "Successfully registered (or logged in)!")
    return redirect("/success")

def success(request):
    return render(request, "logReg/success.html")