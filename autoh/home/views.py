from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from product.models import brands

# Create your views here.

def index(request):
    b_cat =  brands.objects.all()
    print(b_cat)
    for i in b_cat:
        print(i.b_name)
    return render(request,"index.html",{'pro':b_cat})

def login(request):
    print('hellow')
    if request.method == "POST":
        user = request.POST['us_name']
        pas_d = request.POST['p_w']
        valid = auth.authenticate(username = user,password = pas_d)
        if valid is not None:
            auth.login(request,valid) 
            return redirect('/')
        else:
            msg = 'Check Username or Password'
            return render(request,'login.html',{'lng': msg})    
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        userw=request.POST['uname']
        fname=request.POST['fname']
        lname=request.POST['lname']
        emai=request.POST['email']
        paw=request.POST['p_w']
        repaw=request.POST['re-p_w']
        if userw != '' and emai != '' and paw != '':
            if User.objects.filter(username = userw).exists() or User.objects.filter(email = emai).exists():
                msg='User Alredy Exit'
                return render(request,'register.html',{'ms':msg})
            elif paw != repaw:
                msg=" password not match"
                return render(request,'register.html',{'ms':msg})
            else:
                user=User.objects.create_user(username= userw,first_name=fname,last_name=lname,email=emai,password=paw)
                user.save();
                auth.login(request,user)
                return redirect('/')
            
        else:
            msg="Must fill the required coulms"
            return render(request,'register.html',{'ms':msg})
    else:    
        return render(request,'register.html')


    return render(request,"register.html")



def logout(request):
    auth.logout(request)
    return redirect('/')