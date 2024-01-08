from django.shortcuts import render, redirect, get_object_or_404
from . form import UserCreationForm, LoginForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.utils.html import strip_tags
from .models import Entry
from django.core.serializers import serialize
from django.http import JsonResponse


# - Authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def hello_world(request):
    return render(request, 'PassManager/hello_world.html', {})




def login(request):
    form = LoginForm()
    data = {}

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

        data['error'] = {field: strip_tags(message) for field, message in form.errors.items()}


    context = {'loginform':form, 'data':data}

    return render(request, 'PassManager/login.html', context=context) 

def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url="login")
def dashboard(request):
    form = EntryForm()
    uid = request.user.id
    data = Entry.objects.filter(uid=uid)
    if request.method == "POST":
        print(request.user.id)
        if "new-entery" in request.POST:
            form = EntryForm(request.POST)
            
            if form.is_valid():
                form.save()
                return redirect('dashboard')
    context = {"entryform":form,"user":uid,"data":data}

    
    return render(request,'PassManager/dashboard.html',context=context)  

def register(request):
    form = UserCreationForm()
    data ={}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        data['error'] = {field: strip_tags(message) for field, message in form.errors.items()}
    context = {"registerform":form,'data':data}


    return render(request,'PassManager/register.html',context=context)

def getEntryDetails(request):
    id = request.POST.get('id', None)
    try:
        entry = Entry.objects.get(id=id)
        serialized_data = serialize('json', [entry])
        return JsonResponse({'data': serialized_data})
    except Entry.DoesNotExist:
        # return JsonResponse({'message': 'Hai'})
        return JsonResponse({'error': 'Entry not found'}, status=404)

def deleteEntry(request,id):
    entry = get_object_or_404(Entry,pk=id)
    entry.delete()
    # if request.method == 'POST':
    #     entry.delete()
    return redirect('dashboard')
    # return render(request, '', {'entry': entry})



      

# Create your views here.
