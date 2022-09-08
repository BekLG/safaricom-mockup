from re import L
from socket import fromshare
from django import forms

class UserProfile(forms.Form):
    fname = forms.CharField(label='First Name',max_length=50)
    lname = forms.CharField(label='Last Name',max_length=50)
    educationLevel = forms.CharField(label='Education Level',max_length=50)
    age = forms.IntegerField(label='Age')
    sex = forms.CharField(label='Gender',max_length=10)
    phoneNumber = forms.CharField(label='Phonenumber',max_length=20)
    address = forms.CharField(label='Address',max_length=100)
