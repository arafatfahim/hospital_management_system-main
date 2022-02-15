from django.db import models
from django.contrib.auth.models import User
# from hospitalapp.models import Department


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    profile_picture = models.ImageField(upload_to='profile_picture',default='man.png')
    full_name=  models.CharField(max_length=30,null=True,blank=True)
    email= models.EmailField(max_length=60)
    date_joined	= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)


class Doctor(models.Model):
    name = models.CharField(max_length=200)
    # dept = models.OneToOneField(Department, on_delete=models.SET_NULL, null=True)
    speciallist = models.CharField(max_length=200)
    image= models.ImageField(null=True,blank=True, default="avatar.svg")
    details = models.TextField(null=True,blank=True)
    

    def __str__(self):
        return self.name