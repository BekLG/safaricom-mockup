from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserProfile

def getUserInfo(request):
    submitted = False

    if request.method == 'POST':
        form = UserProfile(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form = UserProfile
        if 'submitted' in request.GET:
            submitted = True
    context = {'form':form,'submitted':submitted}
    return render(request,'forms.html',context)

def loadQuestions(request):
    return render(request,'question.html')

def successPage(request):
    return render(request,'success.html')

            


