from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.


def logs(request):
    return render(request,'logs.html')
    
