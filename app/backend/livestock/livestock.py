from django.shortcuts import render
from ..models import Livestock

def livestock_list(request):
    livestock = Livestock.objects.all()
    return render(request, 'app/livestock_list.html', {'livestock': livestock})