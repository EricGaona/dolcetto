from django.urls import path
from . import views

"""
These URLs were been included in the project level URLs file.
"""

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
]