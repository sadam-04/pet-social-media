from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, "pets/index.html")

def profile(request):
    return HttpResponse("profile")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'pets/login.html', {'error': 'Invalid username or password'})
    return render(request, 'pets/login.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'pets/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')