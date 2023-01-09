from . import views
from django.urls import path
from django.contrib.auth import get_user_model
User = get_user_model()


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    ]
