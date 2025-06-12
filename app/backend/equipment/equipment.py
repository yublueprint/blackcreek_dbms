from app.logging.logging import Logger
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from ..models import Equipment

logger = Logger("app/logging/app.log")

@login_required
def equipment_list(request):
    equipment = Equipment.objects.all()
    logger.log(f"User {request.user} viewed equipment list.")
    return render(request, "app/equipment_list.html", {"equipment": equipment})

@login_required
def add_equipment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        type = request.POST.get("type")
        purchase_date = request.POST.get("purchase_date")
        maintenance_due = request.POST.get("maintenance_due")

        Equipment.objects.create(
            name=name,
            type=type,
            purchase_date=purchase_date,
            maintenance_due=maintenance_due,
        )
        logger.log(f"User {request.user} added equipment: {name}")
        return redirect("equipment_list")

@login_required
def edit_equipment(request):
    if request.method == "POST":
        equipment = get_object_or_404(Equipment, id=request.POST.get("id"))
        old_name = equipment.name
        equipment.name = request.POST.get("name")
        equipment.type = request.POST.get("type")
        equipment.purchase_date = request.POST.get("purchase_date")
        equipment.maintenance_due = request.POST.get("maintenance_due")
        equipment.save()
        logger.log(f"User {request.user} edited equipment: {old_name} to {equipment.name}")
        return redirect("equipment_list")

@login_required
def delete_equipment(request):
    if request.method == "POST":
        equipment = get_object_or_404(Equipment, id=request.POST.get("id"))
        equipment_name = equipment.name
        equipment.delete()
        logger.log(f"User {request.user} deleted equipment: {equipment_name}")
        return redirect("equipment_list")