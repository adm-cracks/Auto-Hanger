from django.shortcuts import render,redirect
from .models import brands
from .models import parts
# Create your views here.

def proindex(request):
    part =  request.GET['cat']
    print("part :",part)
    #b_parts = parts.objects.filter(brand=part)
    #print(b_parts)
    ban = brands.objects.get(id=part)
    #return render(request,'product.html',{'br':b_parts,'ban':ban})
    return render(request,'product.html',{'ban':ban})

def prodeta(request):
    pd = request.GET['prbid']
    print("parts details",pd)
    pro_deta = parts.objects.get(id=pd)
    return render(request,'prodeta.html',{'pdet':pro_deta})


def billed(request):
    qua = int(request.GET['num'])
    price = float(request.GET['price'])
    prod = request.GET['product']
   
    print(qua,price,prod)
    print("type",type(qua),type(price))
    total = price * qua
    total = int(total)
    print(total)
    pan = parts.objects.get(id=prod)
    #date
    from datetime import date,datetime
    today =date.today()
    d1=today.strftime("%b-%d-%Y")
    n = datetime.now()
    ct=n.strftime("%I:%M %p")

    return render(request,'bill.html',{'tot':total,'pan':pan,'d1':d1,'ti':ct,'q':qua})