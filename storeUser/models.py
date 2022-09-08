from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(label='First Name',max_length=50)
    lname = models.CharField(label='Last Name',max_length=50)
    educationLevel = models.CharField(label='Education Level',max_length=50)
    age = models.IntegerField(label='Age')
    sex = models.CharField(label='Gender',max_length=10)
    phoneNumber = models.CharField(label='Phonenumber',max_length=20)
    address = models.CharField(label='Address',max_length=100)

    def save(self, *args,**kwargs):
        super().save(*args,**kwargs)
