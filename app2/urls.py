from django.urls import path
from app2.views import *

app_name='app2-string'

urlpatterns=[
    path('app2_string/',app2_string,name='app2_string'),
]