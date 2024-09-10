# Create your models here.
from django.db import models
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

 
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    contact = models.CharField(max_length=250)
    dob = models.DateField(blank=True, null = True)
    land = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null = True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(blank=True, null = True, upload_to= 'images/')
    user_type = models.IntegerField(default = 2)
 
 
    def __str__(self):
        return self.user.username
 
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
 
def save_user_profile(sender, instance, **kwargs):
    print(instance)
    try:
        profile = UserProfile.objects.get(user = instance)
    except Exception as e:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
 
 
###################    
    

# Define choices for various fields
CATEGORY_CHOICES = [
    ('kharif', 'Kharif Crop'),
    # Add other categories as needed
]

NATIONALITY_CHOICES = [
    ('India', 'India'),
    # Add other nationalities as needed
]

SHIPPING_CHOICES = [
    ('fulfilled_by_seller', 'Fulfilled by Seller'),
    ('fulfilled_by_admin', 'Fulfilled by Admin'),
]

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField(upload_to='media/product_images/', blank=True, null=True)
    
    # Product Type
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Quantity in units
    unit = models.CharField(max_length=10, default='kg')  # Unit like kg, g, etc.
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Seller Details
    seller_name = models.CharField(max_length=255)
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    
    # Inventory
    regular_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Shipping
    shipping_type = models.CharField(max_length=50, choices=SHIPPING_CHOICES)
    delivery = models.CharField(max_length=255,default=False)
    selected_state = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self)   :
        return self.title
    
    