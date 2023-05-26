from django.urls import path
from app1.views import *


app_name='string_response'
urlpatterns=[
    path('app1_string/',app1_string,name='app1_string'),

]