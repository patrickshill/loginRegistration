from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, "logReg/index.html")

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
            return redirect("/")
    else:
        if request.method == "POST":
            first_name  = request.POST["first_name"]
            last_name   = request.POST["last_name"]
            email       = request.POST["email"]
            password    = request.POST["password"]

            #create new user
            User.objects.create(first_name=first_name, last_name=last_name,email=email,password=password)

    return redirect("/success")

def login(request):
    return redirect("/success")

def success(request):
    return render(request, "logReg/success.html")