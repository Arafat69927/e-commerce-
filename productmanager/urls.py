from django.urls import path 
from productmanager.views import * 
urlpatterns = [
    path('', home_view, name='home_view'),


    path('categoty_product/', categoty_product, name='categoty_product'),
    path('add_category/', add_category, name='add_category'),   
    path('delete/<str:myid>', delete, name='delete'),
    path('edit/<str:myid>', edit, name='edit'),
    path('product/', product, name='product'),
    path('addproduct/', addproduct, name='addproduct'),

    path('order_view/', order_view, name='order_view'),
    path('addorder/', addorder, name='addorder'), 
    path('delete_order/<str:myid>', delete_order, name='delete_order'),
    path('edit_order/<str:myid>', edit_order, name='edit_order'),


    path('Signup_view/', Signup_view, name='Signup_view'),
    path('login_view/', login_view, name='login_view'),
    path('logout_view/', logout_view, name='logout_view'),

    
    ]