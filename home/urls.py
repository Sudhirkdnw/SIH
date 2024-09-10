from django.contrib import admin  # type: ignore
from django.urls import path, re_path # type: ignore
from django.conf import settings # type: ignore 
from django.contrib.auth import views as auth_views # type: ignore
from django.conf.urls.static import static # type: ignore
from .import views # type: ignore
from django.views.generic.base import RedirectView  # type: ignore

urlpatterns = [
    path('', views.perloader, name='preloader'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('pricing/', views.pricing, name='pricing'),
    path('disease/', views.disease, name='disease'),
    path('blog_detail/', views.blog_detail, name='blogdetail'),
    path('helpcenter/', views.helpcenter, name='helpcenter'),
    path('forget_password/', views.forget_password, name='forgetpassword'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('product/<int:id>/', views.product_details, name='product_details'),

]