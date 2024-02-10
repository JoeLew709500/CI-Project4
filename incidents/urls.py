from . import views
from django.urls import path

urlpatterns = [
    path('', views.IncidentList.as_view(), name='incident_list'),
]