from re import I
import re
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UserProfile

def getUserInfo(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('success')
    else:
        form = UserProfile()
    
    context = {'form':form}
    return render(request,'forms.html',context)

def loadQuestions(request):
    return render(request,'question.html')

def successPage(request):
    return render(request,'success.html')

            


