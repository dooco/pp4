from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
