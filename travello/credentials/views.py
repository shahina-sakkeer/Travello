from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
# REGISTRATION

def register(request):
    if request.method=="POST":
        username=request.POST["username"]
        firstname=request.POST["first_name"]
        lastname=request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password1"]
        cpassword=request.POST["password2"]

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username is already taken")
                return redirect("signup")
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,"This email already exists")
                return redirect("signup")
            
            else:
                user=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
                user.save()
                messages.info(request,"registration completed")
                print("user created")
        else:
            messages.info(request,"password incorrect")
            return redirect("signup")

        return redirect("signin")    
        
    return render(request,"register.html")
# REGISTRATION ENDS

# LOGIN
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("demo")
        else:
            messages.info(request,"invalid username")
            return redirect("signin")
    return render(request,"login.html")    

# LOGIN ENDS

# LOGOUT

def logout(request):
    auth.logout(request)
    return redirect("demo")