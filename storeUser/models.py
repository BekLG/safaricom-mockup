from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    educationLevel = models.CharField(max_length=50)
    age = models.IntegerField(default=0)
    sex = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
