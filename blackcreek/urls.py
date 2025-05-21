from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home(request):
    return redirect('livestock_list')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livestock/', include('blackcreek.features.livestock.urls')),
    path('', home, name='home'),
]