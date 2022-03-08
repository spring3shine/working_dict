from unicodedata import name
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns  = [
    path('', views.index, name='index'),
]
