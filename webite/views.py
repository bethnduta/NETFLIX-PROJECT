from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    url=f'http://www.foxmovies.com/movies/fight-club'
