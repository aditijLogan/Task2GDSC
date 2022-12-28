from django.contrib import admin
from django.urls import path ,include
from info import views

urlpatterns = [
    path('', views.info, name='info'), 
    path('data', views.data, name='data') ,
    path('update/<int:id>',views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    
]