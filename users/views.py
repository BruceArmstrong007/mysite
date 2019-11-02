from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import user
# Create your views here.
def users(request):
    return render(request,'user.html')

def form(request):
    if request.method == "POST":
        name=request.POST.get("name")
        if user_exist(name) == False:
            obj=user()
            obj.name=name
            obj.phone=request.POST.get("phone")
            obj.address=request.POST.get("address")
            obj.designation=request.POST.get("designation")
            obj.bloodgroup=request.POST.get("bloodgroup")
            obj.dateofjoining=request.POST.get("dateofjoining")
            obj.status=request.POST.get("status")
            try:
                obj.save()
            except Exception as e:
                return HttpResponse("<script>alert('Unable to Database."+str(e)+"');</script>")
            else: 
                return HttpResponse("<script>alert('Added to Database.');</script>")
        else:
            return HttpResponse("<script>alert('Already Exist in Database.');</script>")
    else:
        return render(request,'userform.html')    

def display(request):
     context={'user':user.objects.all}
     return render(request,'userlist.html',context)    

def delete(request,tid):
         dele=user.objects.get(tid = tid)
         dele.delete()
         context={'user':user.objects.all}
         return render(request,'userlist.html',context)

def edit(request,tid): 
    edit=user.objects.get(tid = tid) 
    if request.method == "POST":
        try:       
         user.objects.filter(tid = tid).update(name=request.POST.get("name"),phone=request.POST.get("phone"),address=request.POST.get("address"),designation=request.POST.get("designation"),bloodgroup=request.POST.get("bloodgroup"),dateofjoining=request.POST.get("dateofjoining"),status=request.POST.get("status"))
        except Exception as e:
         return HttpResponse("<script>alert('Failed to update in Database."+str(e)+"');</script>")    
        else:
         return HttpResponse("<script>alert('Updated in Database.');</script>")    
    else:
     context={'edit':edit}
     return render(request,'useredit.html',context)
     
#to find if user exist
def user_exist(txtUsername):
   exist_count = user.objects.filter(name = txtUsername).count()
   if exist_count >= 1:
      return True
   else:
      return False