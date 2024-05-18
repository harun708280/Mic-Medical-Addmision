from django.shortcuts import render,redirect
from .forms import *
from django.contrib import messages
# Create your views here.def 

def Registration(request):
    form=registrationForm()
    if request.method == 'POST':
        form=registrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully Registration Done')
            return redirect('login')
        
        else:
            messages.warning(request,'Please Fill up 8 Charecter Password')
            
    return render(request,'registration.html')

def Login(request):
    return render(request,('login.html'))