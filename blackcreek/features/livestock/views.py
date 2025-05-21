from django.http import HttpResponse
from .models import Livestock

def livestock_list(request):
    livestock = Livestock.objects.all()
    names = ", ".join([l.name for l in livestock])
    return HttpResponse(f"Livestock list: {names}")

def livestock_detail(request, pk):
    try:
        livestock = Livestock.objects.get(pk=pk)
        return HttpResponse(f"Livestock detail: {livestock.name}, Age: {livestock.age}, Type: {livestock.type}")
    except Livestock.DoesNotExist:
        return HttpResponse("Livestock not found", status=404)