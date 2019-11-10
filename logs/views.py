from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import log
# Create your views here.


def logs(request):
    context = { 'logs':log.objects.values_list('created_at','log','href','go')}
    return render(request,'logs.html',context)
    
def add(request):
    return render(request,'create.html')    

def edit(request):
    return render(request,'edit.html')   

def delete(request):
    return render(request,'delete.html')
    
