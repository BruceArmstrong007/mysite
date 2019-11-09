from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from .views import travel_list,travel_add,travel_edit,travel_delete,destination_list,destination_add,destination_edit,destination_delete

urlpatterns = [
    path('', travel_list),
    path('add/',travel_add),
    path('edit/<int:tid>/',travel_edit),
    path('delete/<int:tid>/',travel_delete),
    path('destination/',destination_list),
    path('destination/add/',destination_add),
    path('destination/edit/<int:tid>/',destination_edit),
    path('destination/delete/<int:tid>/',destination_delete),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
