from django.urls import path
from .views import *

urlpatterns = [
    path('', community, name='community'),
]