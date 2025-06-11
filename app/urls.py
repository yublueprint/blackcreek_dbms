from django.urls import path

from .backend.crop.crop import crop_list
from .backend.dashboard.dashboard import dashboard
from .backend.equipment.equipment import add_equipment, delete_equipment, edit_equipment, equipment_list 
from .backend.livestock.livestock import add_livestock, delete_livestock, edit_livestock, livestock_list
from .backend.crop.crop import add_crop, delete_crop, edit_crop, crop_list

urlpatterns = [
    path("", dashboard, name="dashboard"),

    # Livestock URLs
    path("livestock/", livestock_list, name="livestock_list"),
    path("livestock/add/", add_livestock, name="add_livestock"),
    path("livestock/edit/", edit_livestock, name="edit_livestock"),
    path("livestock/delete/", delete_livestock, name="delete_livestock"),

    # Crop URLs
    path("crops/", crop_list, name="crop_list"),
    path("crops/add/", add_crop, name="add_crop"),
    path("crops/edit/", edit_crop, name="edit_crop"),
    path("crops/delete/", delete_crop, name="delete_crop"),


    # Equipment URLs
    path("equipment/", equipment_list, name="equipment_list"),  
    path("equipment/add/", add_equipment, name="add_equipment"),
    path("equipment/edit/", edit_equipment, name="edit_equipment"),
    path("equipment/delete/", delete_equipment, name="delete_equipment"),
]
