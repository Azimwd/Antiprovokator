
from django.contrib import admin
from django.urls import path
from sendmessage.views import *

app_name='sendmessage'
urlpatterns = [
    path('', sendmessage, name='index'),
]
