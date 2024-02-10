from . import views
from django.urls import path

urlpatterns = [
    path('', views.incident_list, name='incident_list'),
    path('<int:incident_id>/', views.incident_detail, name='incident_detail'),
]