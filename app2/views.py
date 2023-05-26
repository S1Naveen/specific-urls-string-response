from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app2_string(request):
    return HttpResponse('<h1>app2 string as response</h1>')