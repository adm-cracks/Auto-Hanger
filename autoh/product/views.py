from django.shortcuts import render
from .models import brands
from .models import parts
# Create your views here.

def proindex(request):
    part =  request.GET['cat']
    print(part)
    b_parts = parts.objects.filter(brand=part)
    print(b_parts)
    return render(request,'product.html')