from django.db import models
from django.db import models
from apps.product.models import Product
from apps.vendor.models import Vendor
from django.contrib.auth.models import User
from django.conf import settings


class Order(models.Model):
    status_choices = [
    ('Pending', 'Pending'),    
    ('Cancel', 'Cancel'),
    ('Confirm', 'Confirm'),
    ('Vendor recivied', 'Vendor recivied the order'),
    ('Ready to deliver', 'Ready to deliver'),
    ('Delivered', 'Delivered'),
  
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    paid_amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total')
    vendors = models.ManyToManyField(Vendor, related_name='orders')
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    status = models.CharField(max_length=50, default='Pending', choices=status_choices)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.first_name



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='items', on_delete=models.CASCADE)
    vendor_paid = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return '%s' % self.id
    
    def get_total_price(self):
        return self.price * self.quantity