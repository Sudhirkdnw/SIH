from . import views
from django.contrib import admin
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView


 
urlpatterns = [
    path('redirect-admin', RedirectView.as_view(url="/admin"),name="redirect-admin"),
    path('home', views.home, name="home-page"),
    path('accounts/login',auth_views.LoginView.as_view(template_name="login.html",redirect_authenticated_user = True),name='login'),
    path('userlogin', views.login_user, name="login-user"),
    path('user-register', views.registerUser, name="register-user"),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('profile',views.profile,name='profile'),
    path('update-profile',views.update_profile,name='update-profile'),
    path('update-avatar',views.update_avatar,name='update-avatar'),
    path('farmers', views.farmers, name="farmers"),
    path('add_product', views.add_product, name="add_product"),
    path('product_list', views.product_list, name="product_list"),

    
    
    
]
