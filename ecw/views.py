from django.shortcuts import render,redirect
from .models import CustomerData
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password


def home(request):
    return render(request,'ecw/home.html')

def signup(request):
    if request.method=="POST":
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
    
        if CustomerData.objects.filter(email=email).exists():
            return render(request,'ecw/signup.html',{"error_message":"Email already exists"})


        else:
            CustomerData.objects.create(
            name=name,
            email=email, 
            password=make_password(password)
              )
            return redirect('dashboard')
    else:
        return render(request,'ecw/signup.html')
    
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user=CustomerData.objects.get(email=email)
        except CustomerData.DoesNotExist:
            return render(request,'login.html',{"error_message":"Email dosnt exists"})
        
        if check_password(password, user.password):
            return redirect('dashboard')
       
        else:
            return render(request, 'ecw/login.html', {
                "error_message": "Incorrect password"
            })
        
    else:
        return render(request,'ecw/login.html')


def dashboard(request):
    return render(request,'ecw/dashboard.html')