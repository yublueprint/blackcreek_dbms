from django.shortcuts import render, redirect, get_object_or_404
from ..models import Livestock
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

@login_required
def livestock_list(request):

    livestock = Livestock.objects.all()
    return render(request, "app/livestock_list.html", {"livestock": livestock})


@login_required
def add_livestock(request):
    if request.method == "POST":
        name = request.POST.get("name")
        breed = request.POST.get("breed")
        age = request.POST.get("age")
        health_status = request.POST.get("health_status")

        # Save the new livestock record
        Livestock.objects.create(
            name=name,
            breed=breed,
            age=age,
            health_status=health_status,
        )
        return redirect("livestock_list")


@login_required
def edit_livestock(request):
    if request.method == "POST":
        animal = get_object_or_404(Livestock, id=request.POST.get("id"))
        animal.name = request.POST.get("name")
        animal.breed = request.POST.get("breed")
        animal.age = request.POST.get("age")
        animal.health_status = request.POST.get("health_status")
        animal.save()
        return redirect("livestock_list")


@login_required
def delete_livestock(request):
    if request.method == "POST":
        animal = get_object_or_404(Livestock,  id=request.POST.get("id"))
        animal.delete()  # Delete the record if the method is POST
        return redirect("livestock_list")

