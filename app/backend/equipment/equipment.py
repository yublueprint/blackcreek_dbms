from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Equipment

def equipment_list(request):
    equipment = Equipment.objects.all()
    return render(request, 'app/equipment_list.html', {'equipment': equipment})