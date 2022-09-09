from django import forms
from django.forms import ModelForm
from storeUser.models import UserProfile

class UserProfile(ModelForm):
    fname = forms.TextInput()
    lname = forms.TextInput()
    educationLevel = forms.TextInput()
    age = forms.TextInput()
    sex = forms.TextInput()
    phoneNumber = forms.TextInput()
    address = forms.TextInput()
    
    class Meta:
        model = UserProfile
        fields = ['fname','lname','educationLevel','age','sex','phoneNumber','address']
        labels = {
         'fname':'',
         'lname':'',
         'educationLevel':'',
         'age':'',
         'sex':'',
         'phoneNumber':'',
         'address' :''  
        }
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control','placeholder':'First name'}),
            'lname':forms.TextInput(attrs={'class':'form-control','placeholder':'Last name'}),
            'educationLevel':forms.TextInput(attrs={'class':'form-control','placeholder':'Education level'}),
            'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            'sex':forms.TextInput(attrs={'class':'form-control','placeholder':'Sex'}),
            'phoneNumber':forms.TextInput(attrs={'class':'form-control','placeholder':'Phoen Number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'})
        }
    
