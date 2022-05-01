from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include #include the path for urls in base



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
]
