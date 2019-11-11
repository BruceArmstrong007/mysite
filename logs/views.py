from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import log
import ast

# Create your views here.


def logs(request):
    if request.method == "GET":
        if request.GET.get("delete"):
            log.objects.all().delete()
            return HttpResponse("<script>alert('Logs are deleted');</script>")
        else:
            query = log.objects.values('tid','created_at','log','href','go')
            if query.count() <= 0:
                context = { 'log' : 'Logs are Empty', }
            else: 
                context = { 'logs':query , 'log' : 'Logs',}
    return render(request,'logs.html',context)
    
def add(request,tid):
    arr = []
    arr1 = []
    add=log.objects.filter(tid = tid)
    a = ast.literal_eval(add[0].fields)
    for key, value in a.items(): 
      if key != 'csrfmiddlewaretoken': 
       arr.append(str(key)+" - "+str(value))
    arr1 = ['None']    
    context = { 'logs':add ,'pvalue':arr1,'value':arr}
    return render(request,'logdetails.html',context)

def edit(request,tid):
    arr = []
    arr1 = [] 
    add=log.objects.filter(tid = tid)
    if add[0].fields != None:       
     a = ast.literal_eval(add[0].fields)
     for key, value in a.items(): 
      if key != 'csrfmiddlewaretoken':     
       arr.append(str(key)+" - "+str(value))
    if add[0].pfields != None:       
     b = ast.literal_eval(add[0].pfields)
     for key, value in b.items():  
      arr1.append(str(key)+" - "+str(value))      
    context = { 'logs':add,'value':arr,'pvalue':arr1}
    return render(request,'logdetails.html',context)    

def delete(request,tid):
    arr = [] 
    add=log.objects.filter(tid = tid)
    if add[0].pfields != None:       
     b = ast.literal_eval(add[0].pfields)
     for key, value in b.items():  
      arr.append(str(key)+" - "+str(value))    
    arr1 = ['None']    
    context = { 'logs':add,'pvalue':arr,'value':arr1}
    return render(request,'logdetails.html',context)
    
