from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app1_string(request):
    return HttpResponse('<h1>Specific urls view as Response')

