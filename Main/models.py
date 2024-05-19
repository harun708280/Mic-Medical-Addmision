from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AboutHospital(models.Model):
        
    shortInformation=models.CharField( max_length=200,blank=True,null=True)
    Main_information=models.TextField(blank=True,null= True)
    image=models.ImageField( upload_to='About',blank=True,null=True)
    
    def __str__(self):
        return self.shortInformation

class Doctor(models.Model):
    name=models.CharField( max_length=50)
    title=models.CharField( max_length=50)
    post=models.CharField( max_length=50)
    information=models.TextField(blank=True,null=True)
    facebook=models.URLField(max_length=2000,blank=True,null=True)
    instageram=models.URLField(max_length=2000,blank=True,null=True)
    twiter=models.URLField(max_length=2000,blank=True,null=True)
    linkdin=models.URLField(max_length=2000,blank=True,null=True)
    image=models.ImageField( upload_to=None,blank=True,null=True)
    def __str__(self):
        return self.name
class Deparment(models.Model):
    name=models.CharField( max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Apoinment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    Doctor=models.CharField( max_length=50)
    Department=models.CharField(max_length=50)
    Phone=models.CharField( max_length=50)
    Symptoms=models.CharField( max_length=50)
    upload_date=models.DateField( auto_now_add=True,blank=True,null=True)
    Apoinment_date=models.CharField( max_length=50)
    
    def __str__(self):
        return f'{self.user.username}'

class Tretment(models.Model):
    image=models.ImageField(upload_to=None, )
    title=models.CharField( max_length=100)
    sort_information=models.TextField()
    long_information=models.TextField()
    
    def __str__(self):
        return self.title
    
class benner(models.Model):
    name=models.CharField( max_length=50,blank=True,null=True)
    image=models.ImageField( upload_to=None)
    
    def __str__(self):
        return self.name
    