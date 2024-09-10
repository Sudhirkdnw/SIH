from django.urls import path
from .views import control, home

urlpatterns = [
    path('', home, name='home'),
    path('motor/<str:action>/', control, name='control'),
]
