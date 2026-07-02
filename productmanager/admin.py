from django.contrib import admin
from productmanager.models import *
# Register your models here.
admin.site.register([CustomUserModel,
CategoryModel,
ProductModel,
OrderModel])