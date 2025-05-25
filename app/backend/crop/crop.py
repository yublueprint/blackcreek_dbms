from django.shortcuts import render
from ..models import Crop

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'app/crop_list.html', {'crops': crops})