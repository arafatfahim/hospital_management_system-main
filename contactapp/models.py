from django.db import models
from homeapp.models import Department
from profileapp.models import User
from profileapp.models import Doctor
from datetime import datetime


class Appointment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    patient = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    doctor = models.CharField(max_length=200,null=True, blank=True)
    # date = models.DateField(null=True, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    # time = models.TimeField()
    # updated = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)
    meassage =models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField(null=True, blank=True)
    meassage =models.TextField()

    def __str__(self):
        return self.name
