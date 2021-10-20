  
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('vendor-admin/', views.vendor_admin, name='vendor_admin'),
    path('vendor-order/', views.vendor_order, name='vendor_order'),
    path('vendor-product/', views.vendor_product, name='vendor_product'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
    path('add-product/', views.add_product, name='add_product'),
    path('edit-vendor/', views.edit_vendor, name='edit_vendor'),
    path('edit-product/<int:pk>/', views.edit_product, name='edit_product'),
    path('', views.vendors, name='vendors'),
    path('<int:vendor_id>/', views.vendor, name='vendor'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)