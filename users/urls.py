from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from .views import users,add,edit,delete

urlpatterns = [
    path('', users),
    path('add/',add),
    path('edit/<int:tid>/',edit),
    path('delete/<int:tid>/',delete), 
    path('tasks/',include('travel.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
