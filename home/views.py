from django.shortcuts import render ,get_object_or_404 # type: ignore
from django.http import HttpResponse # type: ignore
from shop.models import Product


# Create your views here.

def perloader(request):
    return render(request,'Frontend/index/preloader.html') 

def index(request):
    return render(request,'Frontend/index/index.html')

def login(request):
    return render(request,'Backend/registration/login.html')

def register(request):
    return render(request,'Backend/registration/register.html')

def aboutus(request):
    return render(request,'Frontend/index/aboutus.html')

def pricing(request):
    return render(request,'Frontend/index/pricing.html')

def shop(request):
    product_list = Product.objects.all()
    context = {'product_list':product_list}
    return render(request,'Frontend/index/shop.html',context)

def product_details(request, id):

    product_details = get_object_or_404(Product, id=id)
    top_product = Product.objects.all().order_by('-id')[:3]
    context = {'product_details':product_details,
               'top_product':top_product,}

    return render(request,'Frontend/index/product_details.html',context)

def disease(request):
    return render(request,'Frontend/index/disease.html')

def blog_detail(request):
    return render(request,'Frontend/index/blogdetail.html')

def helpcenter(request):
    return render(request,'Frontend/index/helpcenter.html')

def forget_password(request):
    return render(request,'Frontend/index/forget_password.html')

def contact(request):
    return render(request,'Frontend/index/contact.html')
