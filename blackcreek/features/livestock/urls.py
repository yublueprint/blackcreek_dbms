from django.urls import path
from . import views

urlpatterns = [
    path('', views.livestock_list, name='livestock_list'),
    path('<int:pk>/', views.livestock_detail, name='livestock_detail'),
]