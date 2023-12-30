from django.shortcuts import render, redirect
from . form import UserCreationForm, LoginForm

# - Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def hello_world(request):
    return render(request, 'PassManager/hello_world.html', {})




def login(request):
    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")


    context = {'loginform':form}

    return render(request, 'PassManager/login.html', context=context) 




def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"registerform":form}


    return render(request,'PassManager/register.html',context=context)        

def dashboard(request):
    
    return render(request,'PassManager/dashboard.html',{})        

# Create your views here.
