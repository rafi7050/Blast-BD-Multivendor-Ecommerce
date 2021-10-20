from django.shortcuts import render
from apps.product.models import Sub_Category, Product
import random
from .forms import CreateUserForm
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login ,logout
from apps.order.models import Order, OrderItem
from apps.order.models import Order, OrderItem
from apps.vendor.models import Vendor
# Create your views here.
def frontpage(request):
    newest_products = Product.objects.all()[0:8]

    return render(request, 'core/frontpage.html', {'newest_products': newest_products})



def registerPage(request):
    #if request.user.is_authenticated:
     #   return redirect('index')

    #else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                user=form.save()
                username =form.cleaned_data.get('username')



                messages.success(request, 'Account is created for ' +  username )
                return redirect('login_cus')

        context = {'form' : form}
        return render(request, 'core/register.html' , context )




def loginPage(request):
    #if request.user.is_authenticated:
        #return redirect('index')

    #else:
        if request.method == 'POST' :
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request ,username = username ,password = password)

           if user is not None:
               login(request , user)
               return redirect('frontpage')

           else:
               messages.info(request, 'Username or Password is incorrect')
        context ={}
        return render(request, 'core/login.html', context)






def customer_order(request):
    customer = request.user
    orders = Order.objects.filter(customer = customer)
    for order in orders:
        order.vendor_amount = 0
        order.vendor_paid_amount = 0
        order.fully_paid = True

        for item in order.items.all():
            
            if item.vendor_paid:
                order.vendor_paid_amount += item.get_total_price()
            else:
                order.vendor_amount += item.get_total_price()
                order.fully_paid = False
    print("abc")        
    print(orders)
    

    return render(request, 'core/customer_order.html', {'orders': orders})


# def vendors(request):
#     vendors = Vendor.objects.all()

#     return render(request, 'core/vendors.html', {'vendors': vendors})

# def vendor(request, vendor_id):
#     vendor = get_object_or_404(Vendor, pk=vendor_id)

#     return render(request, 'core/vendor.html', {'vendor': vendor})
