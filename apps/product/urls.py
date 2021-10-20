from django.urls import path

from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('<slug:sub_category_slug>/<slug:product_slug>/', views.product, name='product'),
    path('<slug:sub_category_slug>/', views.category, name='category'),
    
]
   
