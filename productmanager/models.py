from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUserModel(AbstractUser):
    USER=[
        ('Admin', 'Admin'),
        ('Seller', 'Seller'),
        ('Customer', 'Customer')
    ]
    full_name=models.CharField(max_length=100,null=True)
    role=models.CharField(choices=USER,max_length=100,null=True)
    def __str__(self):
       return f'{self.full_name}'



class CategoryModel(models.Model):
    category_name=models.CharField(max_length=100,null=True)
    description=models.TextField(max_length=200,null=True)
    created_at= models.DateField(auto_now_add=True)
    def __str__(self):
       return f'{self.category_name}'


class ProductModel(models.Model): 
    seller=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True) 
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    product_name=models.CharField(max_length=100,null=True)
    product_description=models.TextField(max_length=100,null=True)
    product_image=models.ImageField(upload_to='media/product_management',null=True)
    price=models.PositiveIntegerField(null=True)
    stock_quantity=models.PositiveIntegerField(null=True) 
    created_at=models.DateField(auto_now_add=True) 
    def __str__(self):
       return f'{self.product_name}'


class OrderModel(models.Model):   
    STATUS=[
        ('Pending','Pending'),
        ('Confirmed','Confirmed'),
        ('Cancelled','Cancelled'),
    ]
    customer=models.ForeignKey(CustomUserModel,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    quantity =models.PositiveIntegerField(null=True)
    total_price =models.PositiveIntegerField(null=True)
    order_status =models.CharField(choices=STATUS, max_length=100, null=True)  
    created_at=models.DateField(auto_now_add=True) 
    def __str__(self):
       return f'{self.customer}'