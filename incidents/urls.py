from . import views
from django.urls import path

urlpatterns = [
    path('', views.incident_list, name='incident_list'),
    path('<int:incident_id>/', views.incident_detail, name='incident_detail'),
    path('incident/new/', views.incident_new, name='incident_new'),
    path('incident/<int:incident_id>/actions/', views.actions, name='actions'),
    path('incident/<int:incident_id>/actions/<int:action_id>', views.action_detail, name='action_detail'),
]       