from django.shortcuts import render, redirect
from .models import Record

def home(request):
    records = Record.objects.all()
    return render(request, 'records/home.html', {'records': records})

def add_record(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Record.objects.create(name=name, email=email)
        return redirect('home')
    return render(request, 'records/add_record.html')
