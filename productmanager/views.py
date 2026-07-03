from django.shortcuts import render,redirect,get_object_or_404
from productmanager.models import *
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home_view(req):

    return render(req,'home.html')

# productMOdel
def addproduct(req):

    return render(req,'addproduct.html')


# CATEGOR MODEL
def categoty_product(req):
    cate_data = CategoryModel.objects.all()
    context={
        'cate_dic':cate_data
    }

    return render(req,'category_product.html',context)

def add_category(req):
    if req.method == 'POST':
        category_title=req.POST.get('category_title')
        descriptoin=req.POST.get('descriptoin')
        created_at=req.POST.get('created_at')

        CategoryModel.objects.create(
            category_name=category_title,
            description=descriptoin,
            created_at=created_at
        )
        return redirect('categoty_product')

    return render(req,'add_category.html')

def order_view(req):
    order_Data = OrderModel.objects.all()
    context={
        'order_dic' : order_Data
    }
    return render(req,'order.html',context)

def delete_order(req,myid):
    delete_ord = OrderModel.objects.filter(id=myid)
    delete_ord.delete()
    return redirect('order_view')

def addorder(req):
    for_product = ProductModel.objects.all()
    
    context={
        'product_dic':for_product
    }
    if req.method=='POST':
       product=ProductModel.objects.get(id=req.POST.get('product'))
       quantity=int(req.POST.get('quantity'))
       
       OrderModel.objects.create(
           customer=req.user,
           product=product,
           quantity=quantity,
           order_status="Pending",
           total_price=product.price*quantity,
           
       )
       return redirect('order_view')
    return render(req, 'addorder.html',context)


# ------------------------------------------------
# Product
def product(req):
    product_data = ProductModel.objects.all()
    context={
        'pro_dic':product_data
    }
    return render(req,'product.html',context)



def addproduct(req):

    if req.method == "POST":
        category = CategoryModel.objects.get(id=req.POST.get("category"))

        ProductModel.objects.create(
            seller=req.user,
            category=category,
            product_name=req.POST.get("product_name"),
            product_description=req.POST.get("product_description"),
            product_image=req.FILES.get("product_image"),
            price=req.POST.get("price"),
            stock_quantity=req.POST.get("stock_quantity"),
        )

        return redirect("product")

    categories = CategoryModel.objects.all()

    return render(req, "addproduct.html", {
        "categories": categories
    })




def delete(req,myid):
    delete_data = CategoryModel.objects.filter(id=myid)
    delete_data.delete()
    return redirect('categoty_product')

def edit(req, myid):
    edit_data = CategoryModel.objects.get(id=myid)

    if req.method == 'POST':
        edit_data.category_name = req.POST.get('category_title')
        edit_data.description = req.POST.get('descriptoin')
        edit_data.save()

        return redirect('categoty_product')   

    context = {
        'edit_dic': edit_data
    }

    return render(req, 'edit.html', context)

# ----------------------------------------------
# AUTH
def Signup_view(req):
    if req.method == "POST":
        username = req.POST.get('username')
        fname=req.POST.get('fname')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')
        role = req.POST.get('role')
        exists = CustomUserModel.objects.filter(username=username).exists()
        if exists:
            messages.warning(req,'Username is Already exists!')
            return redirect('Signup_view')
        
        if password==confirm_password:  
            CustomUserModel.objects.create_user(
                username=username,
                full_name=fname,
                password=password,
                email=email,
                role=role,
            )
  
            messages.success(req, "Account created successfully.")
            return redirect("login_view")
    return render(req,'Signup.html')

def login_view(req):
    if req.method == "POST":

        username= req.POST.get('username')
        password= req.POST.get('password')

        user = authenticate(username=username, password=password)

        print(user)

        if user:
            login(req,user)
            messages.success(req, "Login Successfully!")
            return redirect("home_view")
        else:
            messages.warning(req, "User not found")
            return redirect('login_view')
    return render(req,'login.html')
@login_required
def logout_view(req):
    logout(req)
    messages.success(req, "Successfully Logout!")
    return redirect('login_view')