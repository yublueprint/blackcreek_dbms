from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('livestock/', views.livestock_list, name='livestock_list'),
    path('crops/', views.crop_list, name='crop_list'),
    path('equipment/', views.equipment_list, name='equipment_list'),
]