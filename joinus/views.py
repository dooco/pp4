from django.shortcuts import render, redirect
from django.views import generic
from .models import Review


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def login(request):
    return render(request, 'login.html')
