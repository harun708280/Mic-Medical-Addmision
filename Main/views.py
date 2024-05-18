from django.shortcuts import render,redirect
from django.views import View
from .models import *
# Create your views here.
def home(request):
    about = AboutHospital.objects.all().order_by('-id')[:1]
    doctor = Doctor.objects.all()
    deparment = Deparment.objects.all()
    
    # Initialize variables
    names = ''
    doctors = ''
    deparments = ''
    phone = ''
    symtom = ''
    date = ''
    
    if request.user.is_authenticated:
        if request.method =='POST':
            names = request.POST.get('name')
            doctors = request.POST.get('doctor')
            deparments = request.POST.get('apoinment')
            phone = request.POST.get('phone')
            symtom = request.POST.get('symtoms')
            date = request.POST.get('date')
            user = request.user
            
            
            Apoinments = Apoinment.objects.create(user=user, name=names, Doctor=doctors, Department=deparments, Phone=phone, Symptoms=symtom, Apoinment_date=date)
            Apoinments.save()
            return redirect('home')
  
    return render(request, 'index.html', locals())

class DetailsView(View):
    def get(self, request, pk):
        details = AboutHospital.objects.get(pk=pk)
        return render(request, 'allabout.html', {'details': details})
    
def about(request):
    about=AboutHospital.objects.all().order_by('-id')[:1]
    return render(request,'about.html',locals())