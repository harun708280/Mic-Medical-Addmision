from django.urls import path

from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.home,name='home'),
    path('details/<int:pk>/', views.DetailsView.as_view(), name='details'),
    path('about/',views.about,name='about'),


]+static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
