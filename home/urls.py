from django.contrib import admin
from django.urls import path
from . import views

"""
This URLs was been included in the project level URLs file.
"""

urlpatterns = [
    path('', views.index, name='home')
]