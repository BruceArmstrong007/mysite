from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect


def homepage(request):
    return render(request,'home.html')