from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.conf import settings

# Create your views here.

def userRegister(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect("index")
    context ={
        "form": form,
    }
    return render(request,"register.html",context)

def userLogin(request):
    if request.method == "POST":
        kullanici =request.POST["kullanici"]
        sifre =request.POST["sifre"]
        
        user=authenticate(request, username=kullanici,password=sifre)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            print("Kullanıcı yada şifre yanlış")
            return redirect("login")
    return render(request,"login.html")
        
def userLogout(request):
    logout(request)
    return redirect("index")