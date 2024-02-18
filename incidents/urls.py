from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('incident/', views.incident_list, name='incident_list'),
    path('incident/<int:incident_id>/', views.incident_detail, name='incident_detail'),
    path('incident/new/', views.incident_new, name='incident_new'),
    path('incident/<int:incident_id>/actions/', views.actions, name='actions'),
    path('incident/<int:incident_id>/actions/<int:action_id>/', views.action_detail, name='action_detail'),
    path('incident/<int:incident_id>/actions/new/', views.action_new, name='action_new'),
    path('incident/<int:incident_id>/incidents_delete/', views.incident_delete, name='incident_delete'),
    path('incident/<int:incident_id>/actions/<int:action_id>/delete/', views.action_delete, name='action_delete'),
    path('incident/<int:incident_id>/actions/<int:action_id>/photos/', views.photos, name='photos'),
    path('incident/<int:incident_id>/actions/<int:action_id>/photos/<int:photo_id>', views.photo_delete, name='photo_delete'),
]       