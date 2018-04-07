"""
Definition of urls for Searching
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from . import views

urlpatterns = [
    url(r'^flights',views.flights,name='search_flights'),
    url(r'^luggage',views.luggage,name='search_luggage')
]

