from importlib import import_module

from django.urls import include, path

from django.contrib import admin

from allauth.socialaccount import providers

from . import app_settings
from . import views


urlpatterns = [
    path('', views.Board_featureList.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', views.Board_Detail.as_view(), name='board_detail'),
    path('like/<slug:slug>', views.BoardLike.as_view(), name='board_like'),
    # path("", include("allauth.account.urls"))
    ]