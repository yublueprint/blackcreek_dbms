from django.shortcuts import render, redirect, get_object_or_404
from ..models import Crop
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required  


@login_required 
def crop_list(request):
    crops = Crop.objects.all()
    return render(request, "app/crop_list.html", {"crops": crops})

@login_required
def add_crop(request):
    if request.method == "POST":
        name = request.POST.get("name")
        planting_date = request.POST.get("planting_date")
        harvest_date = request.POST.get("harvest_date") 
        yield_estimate = request.POST.get("yield_estimate") 

        # Save the new record
        Crop.objects.create(
            name=name,
            planting_date=planting_date,
            harvest_date=harvest_date,
            yield_estimate=yield_estimate,
        )
        return redirect("crop_list")
    
@login_required
def edit_crop(request):
    if request.method == "POST":
        crop = get_object_or_404(Crop, id=request.POST.get("id"))
        crop.name = request.POST.get("name")
        crop.planting_date = request.POST.get("planting_date")
        crop.harvest_date = request.POST.get("harvest_date")
        crop.yield_estimate = request.POST.get("yield_estimate")
        crop.save()
        return redirect("crop_list") 
    
@login_required
def delete_crop(request):
    if request.method == "POST":
        crop = get_object_or_404(Crop, id=request.POST.get("id"))
        crop.delete()
        return redirect("crop_list") 



        
