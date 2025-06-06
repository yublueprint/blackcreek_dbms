from django.urls import path

from .backend.crop.crop import crop_list
from .backend.dashboard.dashboard import dashboard
from .backend.equipment.equipment import equipment_list  # <-- Add this line
from .backend.livestock.livestock import add_livestock, delete_livestock, edit_livestock, livestock_list

urlpatterns = [
    path("", dashboard, name="dashboard"),

    # Livestock URLs
    path("livestock/", livestock_list, name="livestock_list"),
    path("livestock/add/", add_livestock, name="add_livestock"),
    path("livestock/edit/", edit_livestock, name="edit_livestock"),
    path("livestock/delete/", delete_livestock, name="delete_livestock"),

    # Crop URLs
    path("crops/", crop_list, name="crop_list"),

    # Equipment URLs
    path("equipment/", equipment_list, name="equipment_list"),  
]
