from django.urls import path
from . import views
from .backend.dashboard.dashboard import dashboard
from .backend.livestock.livestock import livestock_list
from .backend.crop.crop import crop_list
from .backend.equipment.equipment import equipment_list  # <-- Add this line

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('livestock/', livestock_list, name='livestock_list'),
    path('crops/', crop_list, name='crop_list'),
    path('equipment/', equipment_list, name='equipment_list'),  # <-- Add this line
]