from django.shortcuts import render, redirect
from django.views import generic


def login(request):
    return render(request, 'login.html')
