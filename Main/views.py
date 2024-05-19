from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
from django.core.paginator import Paginator
import base64
#from django.http import HttpResponse
#from django.template.loader import get_template
#
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
            return redirect('appointment_details')
  
    return render(request, 'index.html', locals())

class DetailsView(View):
    def get(self, request, pk):
        details = AboutHospital.objects.get(pk=pk)
        return render(request, 'allabout.html', {'details': details})
    
def about(request):
    about=AboutHospital.objects.all().order_by('-id')[:1]
    return render(request,'about.html',locals())

def appointment_details(request):
    appointments = Apoinment.objects.filter(user=request.user).order_by('-id')
    
    if not appointments.exists():
        return redirect('error')
    return render(request, 'apoinmentdetails.html', {'appointments': appointments})



def generate_pdf(request, appointment_id):
    appointment = Apoinment.objects.get(pk=appointment_id)
    template_path = 'pdfapoinment.html'
    context = {'appointment': appointment}
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="appointment_{appointment_id}.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    
    if pisa_status.err:
        return HttpResponse('We had some errors with the PDF generation <pre>' + html + '</pre>')
    return response


def apoinment_delate(request,id):
    apoinment=Apoinment.objects.get(id=id)
    apoinment.delete()
    return redirect('appointment_details')

def Error(request):
    return render(request,'404.html')