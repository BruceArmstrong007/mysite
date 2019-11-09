from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import travel,distance,petrol
from users.models import user


def travel_list(request):
     context={'travel':travel.objects.all()}
     return render(request,'travel.html',context)

def stor(dat): 
         arr = [] 
         if(dat != "None" or False): 
           arr = dat.split(',')
           new = arr[0]
         else:
           new = dat   
         return new  
     
def travel_add(request):
    if request.method == "POST" :
      obj = travel()
      obj.name=request.POST.get("name")
      obj.source=stor(request.POST.get("source"))
      obj.destination1=stor(request.POST.get("destination1"))
      obj.destination2=stor(request.POST.get("destination2", False))
      obj.destination3=stor(request.POST.get("destination3", False))
      obj.destination4=stor(request.POST.get("destination4", False))
      obj.distance=request.POST.get("distance")
      obj.date=request.POST.get("date")
      petrol_price=request.POST.get("petrol_price")
      state=stor(request.POST.get("state"))
      pet = petrol.objects.get(state = state)
      pet.petrol_price=petrol_price
      obj.petrol_price=petrol_price
      obj.total_cost=request.POST.get("total_cost") 
      if request.FILES:
       obj.bill=request.FILES['bill']
      print(request.POST,request.FILES)
      obj.save()
      pet.save()
      return HttpResponse("<script>alert('Successfully Added ');</script>")
    else:
     context={'name': user.objects.values('name'),'distance':distance.objects.all() , 'petrol_price':petrol.objects.all() } 
     return render(request,'traveladd.html',context)  


def travel_edit(request,tid):
    edit = travel.objects.get(tid = tid)
    if request.method == "POST":
      source=request.POST.get("source")
      source=stor(request.POST.get("source"))
      destination1=stor(request.POST.get("destination1"))
      petrol_price=request.POST.get("petrol_price")
      state = stor(request.POST.get("state"))
      pet = petrol.objects.get(state = state)
      pet.petrol_price=petrol_price
      pet.save()
      destination2=stor(request.POST.get("destination2", False))
      destination3=stor(request.POST.get("destination3", False))
      destination4=stor(request.POST.get("destination4", False))
      travel.objects.filter(tid = tid).update(name=request.POST.get("name"),source=source,destination1=destination1,destination2=destination2,destination3=destination3,destination4=destination4,distance=request.POST.get("distance"),date=request.POST.get("date"),petrol_price=petrol_price,total_cost=request.POST.get("total_cost"))
      if request.FILES:
       edit.bill = bill=request.FILES["bill"]
       edit.save()
      return HttpResponse("<script>alert('Successfully Updated ');</script>")    
    else:
     context={'name': user.objects.values('name'),'distance':distance.objects.all() , 'petrol_price':petrol.objects.all() , 'old' : edit} 
     return render(request,'traveledit.html',context)
    

def travel_delete(request,tid):
         dele=travel.objects.filter(tid = tid)
         dele.delete()
         return HttpResponseRedirect('/users/tasks/')


def destination_list(request):
    context={'destination':distance.objects.all()}
    return render(request,'destination.html',context)        


def destination_add(request):
    if request.method == "POST":
      obj = distance()
      obj.address = request.POST.get("address") 
      obj.latitude = request.POST.get("latitude") 
      obj.longitude = request.POST.get("longitude") 
      obj.save()
      return HttpResponse("<script>alert('Successfully Updated ');</script>")
    else:  
     return render(request,'destinationadd.html')    


def destination_edit(request,tid):
    return render(request,'destinationedit.html')    
    
def destination_delete(request,tid):
    return render(request,'destinationdelete.html')

