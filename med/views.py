from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.shortcuts import render,redirect
#from . import forms
from django.contrib import messages
from .models import *
from django.utils import timezone
# Create your views here.

def login_page(request):
    ''' Login page Users '''
    if request.method=="GET":
        return render(request,'med/login.html',{})

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        role=request.POST['Role']

        user=authenticate(username=username,password=password)
        if user:
            if role !=user.profile_user.role:
                messages.error(request,'Incorrect credentials')
                return redirect('med:login')
        else:
            messages.error(request,'Incorrect Username or Password')
            return redirect('med:login')

        django_login(request,user)
        return redirect("med:home")

def logout_view(request):
    ''' logout view '''
    django_logout(request)
    return redirect('med:login')

@login_required(login_url='med:login')
def home(request):
    ''' home page '''
    profile=request.user.profile_user
    medicines=profile.medicine_set.all()
    return render(request,'med/home.html',{'medicines':medicines})

@login_required(login_url='med:login')
def medicine_details(request,id):
    medicine_det=medicine.objects.get(pk=id)
    stocks=stock.objects.get(medicine=medicine_det,user=request.user.profile_user)
    if int(stocks.quantity/stocks.demand)-stocks.lead_time > 0:
        d_to_reorder=int(stocks.quantity/stocks.demand)-stocks.lead_time
    else:
        d_to_reorder=0
    return render(request,'med/medicine_details.html',{'medicine':medicine_det,'stock':stocks,'d_to_reorder':d_to_reorder})

@login_required(login_url='med:login')
def order(request,id):
    medicine_det=medicine.objects.get(pk=id)
    retailers=medicine_det.user.filter(role="retailer").exclude(user=request.user.profile_user)
    distributors=medicine_det.user.filter(role="distributor")
    return render(request,'med/order.html',{'retailers':retailers,'distributors':distributors,'medicine':medicine_det})

@login_required(login_url='med:login')
def place_order(request,med_id,s_id):
    if request.method=="GET":
        seller=UserProfile.objects.get(pk=s_id)
        med=medicine.objects.get(pk=med_id)
        seller_stock=seller.stock.get(medicine=med)
        qty=seller_stock.quantity
        i=10
        values=[]
        for i in range(qty+1):
            values.append(i)
            i=i+10
        return render(request,'med/place_order.html',{'quantity':qty,'seller':seller,'medicine':med,'values':values})

    if request.method=="POST":
        qty=request.POST['Quantity']
        placed_by=request.user.profile_user
        placed_to=UserProfile.objects.get(pk=s_id)
        try:
            med=medicine.objects.get(pk=med_id)
            order=Order()
            order.medicine=med
            order.quantity=qty
            order.status="pending"
            order.placed_by=placed_by
            order.placed_to=placed_to
            order.date_time=timezone.now()
            order.save()
            messages.success(request,'Order Succesfully Placed')
            return redirect('med:recent_orders_p')
        except:
            messages.success(request,'Order Not placed , Unknown Error')
            return redirect('med:recent_orders_p')

@login_required(login_url='med:login')
def recent_orders_p(request):

    if request.method=="GET":
        user=request.user.profile_user
        orders=Order.objects.filter(placed_by=user).order_by('-date_time')
        return render(request,'med/recent_orders.html',{'orders':orders})


@login_required(login_url='med:login')
def recent_orders_r(request):

    user=request.user.profile_user
    orders=Order.objects.filter(placed_to=user).order_by('-date_time')
    return render(request,'med/recent_orders_r.html',{'orders':orders})
