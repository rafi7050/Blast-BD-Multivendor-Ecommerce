from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vendor
from apps.product.models import Product, ProductImage
from .forms import ProductForm, ProductImageForm
# Create your views here.
def vendors(request):
    vendors = Vendor.objects.all()

    return render(request, 'core/vendors.html', {'vendors': vendors})

def vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, pk=vendor_id)

    return render(request, 'core/vendor.html', {'vendor': vendor})


def become_vendor(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)


        if form.is_valid():
            user = form.save()

            login(request, user)

            vendor = Vendor.objects.create(name=user.username, created_by=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'vendor/become_vendor.html', {'form': form})




@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    orders = vendor.orders.filter(status="Pending")
    confirm = vendor.orders.filter(status="Confirm")
    delivered = vendor.orders.filter(status="Delivered")
    
    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False

    return render(request, 'vendor/vendor_admin.html', {'vendor': vendor, 'products': products, 'orders': orders,})
@login_required
def vendor_product(request):
    vendor = request.user.vendor
    products = vendor.products.all()
   

    return render(request, 'vendor/vendor_product_list.html', {'vendor': vendor, 'products': products})

@login_required
def vendor_order(request):
    vendor = request.user.vendor
    orders = vendor.orders.all()
    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            if item.vendor == request.user.vendor:
                if item.vendor_paid:
                    order.vendor_paid_amount += item.get_total_price()
                else:
                    order.vendor_amount += item.get_total_price()
                    order.fully_paid = False
    

    return render(request, 'vendor/vendor_order.html', {'orders': orders})



@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    
    return render(request, 'vendor/add_product.html', {'form': form})


@login_required
def edit_vendor(request):
    vendor = request.user.vendor

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        shop_name = request.POST.get('shop_name', '')
        shop_address = request.POST.get('shop_address', '')
        image = request.POST.get('image', '')

        if name:
            vendor.created_by.email = email
            vendor.created_by.save()

            vendor.name = name
            vendor.shop_name = shop_name
            vendor.shop_address = shop_address
            vendor.image = image
            vendor.save()

            return redirect('vendor_admin')
    
    return render(request, 'vendor/edit_vendor.html', {'vendor': vendor})


@login_required
def edit_product(request, pk):
    vendor = request.user.vendor
    product = vendor.products.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)


       

        if form.is_valid():
            form.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm(instance=product)
      
    
    return render(request, 'vendor/edit_product.html', {'form': form, 'product': product})




