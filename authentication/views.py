from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import re

def home(request):
    return render(request,"authentication/home.html")

def login_page(request):
    return render(request, "authentication/login.html")

def signup_page(request):
    return render(request, "authentication/signup.html")

def signup_logic(request):
    try:
        if request.method=='POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password')
            password2 = request.POST.get('password-confirm')

            common_passwords = ["12345678", "password", "123456789", "qwerty", "abc123", "password1"]


            if username==None or email==None:
                context = {
                    'message': "User name and email should not be empty"
                }
                return render(request, 'authentication/signup.html', context)
            if password1!=password2:
                    
                context = {
                    'message': "Enter same password in confirm passwordrd field"
                }
                return render(request, 'authentication/signup.html', context)
            
            if User.objects.filter(username=username).count()>0:
                context = {
                    'message': "User Name already exists"
                }
                return render(request, 'authentication/signup.html', context)
            
            if User.objects.filter(email=email).count()>0:
                context = {
                    'message': "Email already exists"
                }
                return render(request, 'authentication/signup.html', context)
            
            if len(password1) < 8:
                    context = {
                    'message': "Password must contain at least 8 characters."
                    }
                    return render(request, 'authentication/signup.html', context)
            if re.fullmatch(r"\d+", password1):
                context = {
                'message': "Password can't be a Numeric."
                }
                return render(request, 'authentication/signup.html', context)
            if password1.lower() in common_passwords:
                context = {
                'message': "Password can't be a commonly used password."
                }
                return render(request, 'authentication/signup.html', context)



            userObj = User.objects.create_user(username=username, email=email, password=password1)
            userObj.save()

            return redirect('/login')
    except Exception as e:
        context = {
                    'message': str(e)
                }
        return render(request, 'authentication/signup.html', context)


def credentials_check(request):
    try:
        if request.method == 'POST':

            username_or_email = request.POST.get('email')
            password = request.POST.get('password')
            print(username_or_email + "-->" + password)


            user = User.objects.filter(email=username_or_email).first()
            if user:
                username = user.username  
            else:
                username = username_or_email

            user = authenticate(username=username, password=password)
  

            if user is not None:
                login(request=request, user=user)
                return redirect('/dashboard')
            else:
                context = {
                    'message': "Entered wrong credentials"
                }
                return render(request, "authentication/login.html", context)
    except Exception as e:
        print(f"Exception occurred: {e}")  # Log the exception
        return redirect('/login')

def dashboard(request):
    if request.user.is_authenticated:
        context = {
            "user": request.user 
        }
        return render(request, 'authentication/dashboard.html', context)
    else:
        return redirect("/login")
    
def profile(request):
    if request.user.is_authenticated:  
        context = {
            "user": request.user  
        }
        return render(request, 'authentication/profile.html', context)
    else:
        return render(request, 'authentication/login.html')
    
def change_password(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "authentication/change_password.html")

def logout_user(request):
    logout(request)
    return redirect("/")

def reset_password(request):
    try:
        if request.method=="POST" and request.user.is_authenticated:
            old_password = request.POST.get('old_password')
            new_password = request.POST.get('new_password')
            new_password_confirm = request.POST.get('new_password_confirm')

            user = request.user

            if user.check_password(old_password):
                if new_password == new_password_confirm:
                    user.set_password(new_password)
                    user.save()
                    return redirect("/dashboard")
                else:
                    context = {
                    "message": "New password and confirm password should be same"
                }
                return render(request, "authentication/check_password.html", context)
            else:
                context = {
                    "message": "Old password is Wrong"
                }
                return render(request, "authentication/check_password.html", context)
    except Exception as e:
        return redirect("/change_password")
