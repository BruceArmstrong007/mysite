from django.http import HttpResponse,QueryDict
from django.shortcuts import render
from django.http import HttpResponseRedirect
from logs.models import log
from .models import user
# Create your views here.

def users(request):
     context={'user':user.objects.all() }
     return render(request,'users.html',context) 

def add(request):
    if request.method == "POST":
        phone=request.POST.get("phone")
        if user_exist(phone) == False:
            obj=user()
            obj.name=request.POST.get("name")
            obj.phone=phone
            obj.address=request.POST.get("address")
            obj.designation=request.POST.get("designation")
            obj.bloodgroup=request.POST.get("bloodgroup")
            obj.dateofjoining=request.POST.get("dateofjoining")
            obj.status=request.POST.get("status")
            obj.save()
            ob = log()
            ob.log = obj.tid
            ob.fields = QueryDict(request.body).dict()
            ob.href = '/users/add/'
            ob.go = '/logs/add/'
            ob.save()
            return HttpResponse("<script>alert('Successfully Added ');</script>")
        else:
            return HttpResponse("<script>alert('Already Exist');</script>")
    else:
        return render(request,'useradd.html')      

def delete(request,tid):
         dele=user.objects.filter(tid = tid)
         dele.delete()
         ob = log()
         ob.log = tid
         ob.fields = QueryDict(request.body).dict()
         ob.href = '/users/'
         ob.go = '/logs/delete/'
         ob.save()
         return HttpResponseRedirect('/users/')

def edit(request,tid): 
    edit=user.objects.get(tid = tid) 
    if request.method == "POST":
         user.objects.filter(tid = tid).update(name=request.POST.get("name"),phone=request.POST.get("phone"),address=request.POST.get("address"),designation=request.POST.get("designation"),bloodgroup=request.POST.get("bloodgroup"),dateofjoining=request.POST.get("dateofjoining"),status=request.POST.get("status"))  
         ob = log()
         ob.log = tid
         ob.fields = QueryDict(request.body).dict()
         ob.href = '/users/edit/'
         ob.go = '/logs/edit/'
         ob.save()
         return HttpResponse("<script>alert('Successfully Updated ');</script>")    
    else:
     context={'edit':edit}
     return render(request,'useredit.html',context)
     
#to find if user exist
def user_exist(phone):
   exist_count = user.objects.filter(phone = phone).count()
   if exist_count >= 1:
      return True
   else:
      return False