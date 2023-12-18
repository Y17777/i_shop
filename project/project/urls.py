from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path("accounts/", include("accounts.urls")),
    # path('pages/', include('django.contrib.flatpages.urls')),
    path('products/', include('simpleapp.urls')),
]
#yandex pas: skTest11tt pass test_BlS4812s