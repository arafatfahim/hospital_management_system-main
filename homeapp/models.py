from django.db import models
from profileapp.models import Doctor

class Department(models.Model):
    name = models.CharField(max_length=200)
    image= models.ImageField(null=True,blank=True, default="avatar.svg")
    details=models.TextField()
    
    deptdoctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True,related_name='doctor_name')

    def __str__(self):
        return self.name


class Laboratory(models.Model):
    testname=models.CharField(max_length=100)
    costoftest=models.IntegerField(blank=True, null=True)
    resulttime=models.TimeField()

class Ambulance(models.Model):
    name= models.CharField(max_length=50)
    number= models.IntegerField(blank=True, null=True)


class services(models.Model):
    laboratory=models.ForeignKey(Laboratory, on_delete=models.CASCADE, null=True,blank=True)
    ambulance=models.ForeignKey(Ambulance,on_delete=models.CASCADE,null=True,blank=True,related_name='lab_name')
    doctorlist=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True,related_name='amb_name')
    sergery= models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True,blank=True,related_name='ser_name')


class Gallery(models.Model):
    image=models.ImageField(upload_to='gallery_img', blank=True, null=True)
    title=models.CharField( max_length=20, blank=True, null=True)
    text=models.CharField(max_length=50, blank=True, null=True)


class Review(models.Model):
    name=models.CharField( max_length=20, blank=True, null=True)
    title=models.CharField( max_length=20, blank=True, null=True)
    text=models.CharField(max_length=50, blank=True, null=True)
