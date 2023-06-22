from importlib import import_module

from django.urls import include, path

from django.contrib import admin

from allauth.socialaccount import providers

from . import app_settings
from . import views


urlpatterns = [
    # path('', views.BoardFeatureList.as_view(), name='home'),
    path('', views.all_posts, name='all_posts'),
    path('admin/', admin.site.urls),
    # path('<slug:slug>/', views.category_detail, name='category_detail'),
    path('board/<slug:slug>/', views.BoardDetail.as_view(), name='board_detail'),
    path('like/<slug:slug>', views.BoardLike.as_view(), name='board_like'),
    path('<slug:category_slug>/<slug:slug>/', views.BoardDetail.as_view(), name='feature_detail'),
    path('new/', views.PostCreate.as_view(), name='post_new'),
    path('board/<slug:slug>', views.PostUpdate.as_view(), name='post_edit'),
    path('delete/<slug:slug>', views.PostDelete.as_view(), name='post_delete'),
    ]
