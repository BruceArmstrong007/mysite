from django.contrib import admin
from django.db import models
from .models import travel,distance,petrol

admin.site.register(travel)
admin.site.register(distance)
admin.site.register(petrol)