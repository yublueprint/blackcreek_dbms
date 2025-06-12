from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from app.logging.logging import Logger

from ..models import Supplies

logger = Logger("app/logging/app.log")

@login_required
def supplies_list(request):
    supplies = Supplies.objects.all()
    logger.log(f"User {request.user} viewed supplies list.")
    return render(request, "app/supplies_list.html", {"supplies":supplies})

@login_required
def add_supplies(request):
    if request.method == "POST":
        name = request.POST.get("name")
        type = request.POST.get("type")
        quantity = request.POST.get("quantity")
        unit = request.POST.get("unit")
        
        Supplies.objects.create(
            name=name,
            type=type,
            quantity=quantity,
            unit=unit,
        )
        logger.log(f"User {request.user} added supply: {name}")
        return redirect("supplies_list")

@login_required
def edit_supplies(request):
    if request.method == "POST":
        supply = get_object_or_404(Supplies,id=request.POST.get("id"))
        old_name = supply.name
        supply.name = request.POST.get("name")
        supply.type = request.POST.get("type")
        supply.quantity = request.POST.get("quantity")
        supply.unit = request.POST.get("unit")
        supply.save()
        logger.log(
            f"User {request.user} edited supply: {old_name} to {supply.name}"
        )
        return redirect("supplies_list")

@login_required
def delete_supplies(request):
    if request.method=="POST":
        supply = get_object_or_404(Supplies, id=request.POST.get("id"))
        supply_name = supply.name
        supply.delete()
        logger.log(f"User {request.user} deleted supply: {supply_name}")
        return redirect("supplies_list")