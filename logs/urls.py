from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from .views import add,edit,delete,logs

urlpatterns = [
    path('', logs),
    path('add/<int:tid>/',add),
    path('edit/<int:tid>/',edit),
    path('delete/<int:tid>/',delete),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
