from re import I
import re
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import UserProfile

def getUserInfo(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)

        if form.is_valid():
            form.save()
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            educationLevel = form.cleaned_data['educationLevel']
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            phoneNumber = form.cleaned_data['phoneNumber']
            address = form.cleaned_data['address']

            return HttpResponseRedirect('question/register/success')
        else:
            form = UserProfile()
        
        context = {'form':form}
        return render(request,'forms.html',context)

def loadQuestions(request):
    return render(request,'question.html')

def successPage(request):
    return render(request,'success.html')


            


