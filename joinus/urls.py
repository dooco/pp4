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
    path('rate/<slug:slug>', views.BoardLike.as_view(), name='board_like'),
    # path("", include("allauth.account.urls"))
    ]

if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [path("social/", include("allauth.socialaccount.urls"))]

# Provider urlpatterns, as separate attribute (for reusability).
provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + ".urls")
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, "urlpatterns", None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns