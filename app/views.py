from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Livestock, Crop, Equipment

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def livestock_list(request):
    livestock = Livestock.objects.all()
    return render(request, 'app/livestock_list.html', {'livestock': livestock})

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'app/crop_list.html', {'crops': crops})

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'app/equipment_list.html', {'equipment': equipment})
