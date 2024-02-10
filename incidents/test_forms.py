from django.test import TestCase
from .forms import IncidentForm, ActionForm

class TestIncidentForm(TestCase):
    def test_incident_form(self):
        form = IncidentForm({
            'location': 'Test Location',
            'incident_category': 1,
            'received_on': '2021-01-01T00:00',
            'details': 'Test Details',
        })
        self.assertTrue(form.is_valid(), msg=form.errors)
        