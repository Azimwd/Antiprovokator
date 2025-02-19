
from xml.dom.expatbuilder import Namespaces
from django.contrib import admin
from django.urls import path
from main.views import *

app_name='main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
]
