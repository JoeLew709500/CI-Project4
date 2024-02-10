from django.shortcuts import render
from django.views import generic
from .models import Incident, Action

# Create your views here.

class IncidentList(generic.ListView):
    model = Incident
    template_name = 'incident/index.html'
    paginate_by = 10
