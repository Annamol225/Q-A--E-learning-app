from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate


def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        first_name=request.POST.get('name')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already taken ')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken ')
                return redirect('signup')

            user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
            user.save()
            user=authenticate(username=username,password=password1)
            if user is not None:
                auth.login(request,user)
                return redirect('/')
        else: 
            messages.info(request,'Please enter same password')
            return redirect('signup')              
                
    return render(request,'signup.html')


def login(request):
    if request.method=='POST':
        username=request.POST.get('username')         
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalude password')
            return redirect('login')  
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
    
