from django.shortcuts import render
from .models import productdata
from .forms import Insertingdata,updatingdata,deletingdata
from django.http.response import HttpResponse
def index_view(request):
    return render(request,'index.html')
def inserting_view(request):
    if request.method=="POST":
        iform=Insertingdata(request.POST)
        if iform.is_valid():
            product_id=request.POST.get('product_id')
            product_name=request.POST.get('product_name')
            product_class=request.POST.get('product_class')
            product_color=request.POST.get('product_color')
            product_cost=request.POST.get('product_cost')
            data=productdata(
                product_id=product_id,
                product_name=product_name,
                product_class=product_class,
                product_color=product_color,
                product_cost=product_cost
            )
            data.save()
            iform=Insertingdata()
            return render(request,'insertingdata.html',{'iform':iform})
        else:
            return HttpResponse("invalid user data")
    else:
        iform=Insertingdata()
        return render(request,'insertingdata.html',{'iform':iform})
def retrive_view(request):
    products=productdata.objects.all()
    return render(request,'retrieving-data.html',{'products':products})
def update_view(request):
    if request.method=="post":
        uform=updatingdata(request.post)
        if uform.is_valid():
            product_id=request.POST.get('product_id')
            product_cost=request.POST.get('product_cost')
            pdata=productdata.objects.filter(product_id=product_id)
            if pdata:
                pdata.updata(product_cost=product_cost)
                uform=updatingdata()
                return render(request,'updateform.html',{'uform':uform})
            else:
                return HttpResponse("invalid productId")
        else:
            return HttpResponse("user invalid data")

    else:
        uform=updatingdata()
        return render(request,'updateform.html',{'uform':uform})

