from django.forms import ModelForm

from apps.product.models import Product, ProductImage

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['sub_category', 'title', 'description', 'price', 'image', 'image_2', 'image_3', 'image_4', 'image_5', 'image_6', 'image_7', 'image_8']

class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']