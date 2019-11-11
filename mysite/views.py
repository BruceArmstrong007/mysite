from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from users.models import user
from travel.models import travel,distance
def homepage(request):
    ucount = travel.objects.all().count()
    lcount = distance.objects.all().count()
    tcount = travel.objects.all().count()
    print(lcount)
    print(tcount)
    context = { 'users': ucount ,'travel':tcount,'distance': lcount }
    return render(request,'home.html',context)