from .models import Incident, Action
from django import forms    

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['location', 'incident_category', 'received_on', 'details','closed_on']

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['incident', 'action_code', 'details', 'completed', 'completed_on']