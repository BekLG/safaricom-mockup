from django.db import models

class UserProfile(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    educationLevel = models.CharField(max_length=50)
    age = models.CharField(max_length=12)
    sex = models.CharField(max_length=10)
    phoneNumber = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.fname +" "+self.lname