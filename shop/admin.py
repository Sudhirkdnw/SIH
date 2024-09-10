import django
from django.contrib import admin
from shop.models import UserProfile
from shop.models import Product
 
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Product)