from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from .models import *


def home(request):
    return render(request,'home.html')


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
            
        else:
            messages.info(request,"passwords are not the same")
            return redirect('register')
    else:
        return render(request,'register.html')


def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login')
        
    else:
       return render (request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def cart(request):
    return render(request,'cart.html')

def careers(request):
    return render(request,'careers.html')

def aboutus(request):
    return render(request,'aboutus.html')


def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)  # Fetch the logged-in user's profile
    return render(request, 'profile.html', {"user": user_profile})


def products(request):
    ordered_products = SaleOrder.objects.values_list('product_id', flat=True)
    available_products = ProductMaster.objects.exclude(product_id__in=ordered_products)
    bins = BinMaster.objects.prefetch_related('productmaster_set').all()

    # Organizing bins with their products
    bins_with_products = {}
    for bin in bins:
        bins_with_products[bin] = bin.productmaster_set.all()  # Get all products in this bin

    context = {
        'bins_with_products': bins_with_products,
        'products': available_products,
    }
    return render(request, 'products.html', context)



def order_product(request, product_id):
    product = ProductMaster.objects.get(product_id=product_id)
    
    # Assume customer is logged in (update based on authentication)
    customer = CustomerMaster.objects.first()  # Replace with `request.user.customer` if using Django auth

    # Example: Ordering 5 tons
    quantity_ordered = 5

    # Generate a unique sale order ID
    sale_order_id = f"SO{uid4().hex[:6].upper()}"  

    # Create a new order entry
    SaleOrder.objects.create(
        sale_order_id=sale_order_id,
        sale_order_date=now().date(),
        customer=customer,
        product=product,
        sale_order_qty_in_tons=quantity_ordered
    )

    # Update product stock
    product.stock_in_tons -= quantity_ordered
    product.save()

    return redirect('products')


