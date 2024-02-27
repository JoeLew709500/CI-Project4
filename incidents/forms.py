from django import forms
from .models import Incident, Action, INCIDENT_CATEGORY_CHOICES, ActionPhoto


INCIDENT_CATEGORY_CHOICES = ((0, 'All'),) + INCIDENT_CATEGORY_CHOICES

class IncidentForm(forms.ModelForm):
    """
    
    Form to create and update an incident

    """
    class Meta:
        """
        Meta class for IncidentForm
        """
        model = Incident
        fields = ['location', 'incident_category','received_on', 'details','closed_on']

        widgets = {
            'received_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'closed_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ActionForm(forms.ModelForm):
    """

    Form to update an action
    
    """
    class Meta:
        """
        Meta class for ActionForm
        """
        model = Action
        fields = ['incident', 'action_code', 'details', 'completed_on']

        widgets = {
            'completed_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class ActionFormNew(forms.ModelForm):
    """

    Form to create new action

    """
    class Meta:
        """
        Meta class for ActionFormNew
        """
        model = Action
        fields = ['action_code', 'details', 'completed_on']

        widgets = {
            'completed_on': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class IncidentFormSearch(forms.Form):
    """
    
    Form to search for incident

    """
    incident_category = forms.ChoiceField(choices=INCIDENT_CATEGORY_CHOICES)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),
                           required=False)

class PhotoForm(forms.ModelForm):
    """
    
    Form to add photos to actions
    
    """
    class Meta:
        """
        Meta class for PhotoForm
        """
        model = ActionPhoto
        fields = ['photo']
