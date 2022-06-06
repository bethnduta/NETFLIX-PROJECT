
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import AbstractUser


# Create your views here.
class Home(View):
    def get(self,request,*args, **kwargs):
        return render(request,'index.html')

  