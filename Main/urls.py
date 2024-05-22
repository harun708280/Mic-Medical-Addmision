from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.home,name='home'),
    path('details/<int:pk>/', views.DetailsView.as_view(), name='details'),
    path('about/',views.about,name='about'),
    #path('apoinment-details/',views.appointment_details,name='apoinment-details'),
    path('eror/',views.Error,name='error'),
    path('apoinment-delate/<int:id>/', views.apoinment_delate, name='apoinment-delate'),
    path('appointments/',views. appointment_details, name='appointment_details'),
    path('appointments/pdf/<int:appointment_id>/',views. generate_pdf, name='generate_pdf'),
    path('treatment/',views.tretment,name='treatment'),
    path('tretment-details/<int:pk>/',views.tretmentView.as_view(),name='tretment-details'),
    path('update/<int:id>/',views.Update,name='update'),
    path('update/updateSave/<int:id>/',views.UpdateSave,name='update-save')
    

]+static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
