from django.contrib import admin
from django.urls import path, include
from .views import chat_with_ai,order
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from .import views


urlpatterns = [
    path('', chat_with_ai, name='chat_with_ai'),
    path('order', order, name='order'),
    path('accounts/login',auth_views.LoginView.as_view(template_name="Backend/registration/login.html",redirect_authenticated_user = True),name='login'),


] 