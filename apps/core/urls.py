from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
   # path('contact/', views.contact, name='contact')
    path('register_cus/', views.registerPage , name='register_cus'),
    path('login_cus/', views.loginPage , name='login_cus'),
    path('customer-order/', views.customer_order, name='customer_order'),
    # path('vendors', views.vendors, name='vendors'),
    # path('<int:vendor_id>/', views.vendor, name='vendor'),
   
   
     
]