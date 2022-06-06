
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path,include

from webite.apps import WebiteConfig



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('webite.urls')),
]
