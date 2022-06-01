
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from webite.apps import WebiteConfig


def home(request):
    return HttpResponse('home')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
]
