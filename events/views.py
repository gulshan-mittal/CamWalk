from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
import bcrypt
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return render(request, 'events/signup.html', {})


def index(request):
    return render(request, 'events/index.html')

def register(request):
    errors = User.objects.validator(request.POST)
    print(errors)
    if len(errors):
        for tag, error in errors.items():
            messages.error(request, error, extra_tags=tag)
        return redirect('/events/index')
    
    hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User()
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.password = hashed_password
    user.email = request.POST['email']
    user.save()
    # user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], password=hashed_password, email=request.POST['email'])
    # user.save()
    request.session['id'] = user.id
    print("Gulshan")
    return redirect('/events/success')

def login(request):
    if (User.objects.filter(email=request.POST['login_email']).exists()):
        user = User.objects.filter(email=request.POST['login_email'])[0]
        if (bcrypt.checkpw(request.POST['login_password'].encode(), user.password.encode())):
            request.session['id'] = user.id
            return redirect('/events/success')
    return redirect('/events/index')

def success(request):
    user = User.objects.get(id=request.session['id'])
    context = {
        "user": user
    }
    return render(request, 'events/success.html', context)

def eventdetails(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return render(request, 'events/eventdetails.html', {})

def cameradetails(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    return render(request, 'events/cameradetails.html', {})

