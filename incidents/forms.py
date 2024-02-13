from .models import Incident, Action, INCIDENT_CATEGORY_CHOICES, ActionPhoto
from django import forms

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['location', 'incident_category','received_on', 'details','closed_on']

        widgets = {
            'received_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'closed_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['incident', 'action_code', 'details', 'completed_on']

        widgets = {
            'completed_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ActionFormNew(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['action_code', 'details', 'completed_on']

        widgets = {
            'completed_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class IncidentFormSearch(forms.Form):
    incident_category = forms.ChoiceField(choices=INCIDENT_CATEGORY_CHOICES)

class PhotoForm(forms.ModelForm):
    class Meta:
        model = ActionPhoto
        fields = ['photo']