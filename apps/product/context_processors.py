from apps.product.models import Category, Sub_Category

from django.shortcuts import render
def menu_categories(request):

    categories = Category.objects.all()
    sub_categories = Sub_Category.objects.all()

    return {'menu_categories': categories, 'sub_categories': sub_categories}