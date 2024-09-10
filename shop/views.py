import os 
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product

from shop.models import UserProfile
from shop.forms import UserRegistration, UpdateProfile, UpdateProfileMeta, UpdateProfileAvatar, AddAvatar
from django.utils.text import slugify

from django.core.files.storage import default_storage 
context = {
    'page_title' : 'Blog Site'
}
 
# Create your views here.
@login_required
def home(request):
    farmers = UserProfile.objects.all().order_by('-id')[:10]
    context = {'farmers':farmers}

    return render(request, 'Backend/home.html',context)
 
def login_user(request):
    logout(request)
    resp = {"status":'failed','msg':''}
    username = ''
    password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
 
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status']='success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp),content_type='application/json')
 
#Logout
def logoutuser(request):
    logout(request)
    return redirect('/')
 
def registerUser(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home-page')
    context['page_title'] = "Register User"
    if request.method == 'POST':
        data = request.POST
        form = UserRegistration(data)
        if form.is_valid():
            form.save()
            newUser = User.objects.all().last()
            try:
                profile = UserProfile.objects.get(user = newUser)
            except:
                profile = None
            if profile is None:
                UserProfile(user = newUser, dob= data['dob'], contact= data['contact'], address= data['address'], avatar = request.FILES['avatar']).save()
            else:
                UserProfile.objects.filter(id = profile.id).update(user = newUser, dob= data['dob'], contact= data['contact'], address= data['address'])
                avatar = AddAvatar(request.POST,request.FILES, instance = profile)
                if avatar.is_valid():
                    avatar.save()
            username = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password1')
            loginUser = authenticate(username= username, password = pwd)
            login(request, loginUser)
            return redirect('home-page')
        else:
            context['reg_form'] = form
 
    return render(request,'Backend/registration/register.html',context)
 
@login_required
def profile(request):
    context = {
        'page_title':"My Profile"
    }
 
    return render(request,'Backend/profile.html',context)
 
@login_required
def update_profile(request):
    context['page_title'] = "Update Profile"
    user = User.objects.get(id= request.user.id)
    profile = UserProfile.objects.get(user= user)
    context['userData'] = user
    context['userProfile'] = profile
    if request.method == 'POST':
        data = request.POST
        form = UpdateProfile(data, instance=user)
        if form.is_valid():
            form.save()
            form2 = UpdateProfileMeta(data, instance=profile)
            if form2.is_valid():
                form2.save()
                messages.success(request,"Your Profile has been updated successfully")
                return redirect("profile")
            else:
                context['form2'] = form2
        else:
            context['form1'] = form
            form = UpdateProfile(instance=request.user)
    return render(request,'Backend/update_profile.html',context)
 
 
@login_required
def update_avatar(request):
    context['page_title'] = "Update Avatar"
    user = User.objects.get(id= request.user.id)
    context['userData'] = user
    context['userProfile'] = user.profile
    img = user.profile.avatar.url
    old_avatar = user.profile.avatar.name
    context['img'] = img
    if request.method == 'POST':
        form = UpdateProfileAvatar(request.POST, request.FILES,instance=user)
        if form.is_valid():
            avatar_file = request.FILES.get('avatar')
            if avatar_file:
                filename, extension = os.path.splitext(avatar_file.name)
                new_filename = f"{slugify(user.username)}-avatar{extension}"
                user.profile.avatar.save(new_filename, avatar_file)
            form.save()
            if default_storage.exists(old_avatar):
                default_storage.delete(old_avatar)
            messages.success(request,"Your Profile has been updated successfully")
            return redirect("profile")
        else:
            context['form'] = form
            form = UpdateProfileAvatar(instance=user)
    return render(request,'Backend/update_avatar.html',context)

########################################## ADD FARMERS  #########################################
def farmers(request):
    farmers = UserProfile.objects.all()
    context = {'farmers':farmers}
    return render(request, 'Backend/farmers.html',context)

########################################## ADD PRODUCTS  #########################################
def add_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        images = request.FILES.getlist('images')  # To handle multiple files
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        unit = request.POST.get('unit')
        price_per_unit = request.POST.get('price_per_unit')
        
        seller_name = request.POST.get('seller_name')
        nationality = request.POST.get('nationality')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        email = request.POST.get('email')
        
        regular_price = request.POST.get('regular_price')
        sale_price = request.POST.get('sale_price')
        
        shipping_type = request.POST.get('shipping_type')
        delivery = 'delivery' in request.POST
        selected_state = request.POST.get('selected_state')

        # Create and save the Product instance
        product = Product.objects.create(
            title=title,
            description=description,
           
            category=category,
            quantity=quantity,
            unit=unit,
            price_per_unit=price_per_unit,
            seller_name=seller_name,
            nationality=nationality,
            contact_number=contact_number,
            address=address,
            email=email,
            regular_price=regular_price,
            sale_price=sale_price,
            shipping_type=shipping_type,
            delivery=delivery,
            selected_state=selected_state,
            
        )
        
        # Handle the images separately (if multiple images are allowed)
        for image in images:
            product.images.save(image.name, image)

        return redirect('/shop/home')  # Redirect after saving

    return render(request, 'Backend/add_product.html')  # Render your form template


def product_list(request):
    product_list = Product.objects.all()
    context = {'product_list':product_list}
    return render(request, 'Backend/product_list.html',context)