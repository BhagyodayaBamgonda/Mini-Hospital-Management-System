from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import User

def home(request):
    return render(request,'home.html')

def signup(request):

    if request.method=='POST':

        username=request.POST['username']
        password=request.POST['password']
        role=request.POST['role']

        user=User.objects.create_user(
        username=username,
        password=password,
        role=role
        )

        login(request,user)

        if role=="doctor":
            return redirect('doctor_dashboard')
        else:
            return redirect('patient_dashboard')

    return render(request,'signup.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            if user.role == "doctor":
                return redirect("doctor_dashboard")
            else:
                return redirect("patient_dashboard")

    return render(request, "login.html")