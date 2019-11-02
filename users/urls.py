from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from .views import users,form,display,edit,delete

urlpatterns = [
    path('', users),
    path('form/',form),
    path('list/',display),
    path('list/edit/<int:tid>/',edit),
     path('list/delete/<int:tid>/',delete), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
