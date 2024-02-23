from django.contrib.auth.models import User
from django.test import TestCase
from .forms import IncidentForm, ActionForm
from .models import Incident

class TestIncidentForm(TestCase):
    """
    Test Incident Form
    """
    def test_incident_form(self):
        form = IncidentForm({
            'location': 'Test Location',
            'incident_category': 1,
            'received_on': '2021-01-01T00:00',
            'details': 'Test Details',
        })
        self.assertTrue(form.is_valid(), msg=form.errors)
    
    def test_incident_form_invalid(self):
        form = IncidentForm({
            'location': True,
            'incident_category': 'p',
            'received_on': 'dasd',
        })
        self.assertFalse(form.is_valid(), msg=form.errors)
        self.assertEqual(form.errors['details'], ['This field is required.'])

class TestActionForm(TestCase):
    """
    Test Action Form
    """
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.incident = Incident.objects.create(
            location='Test Location',
            incident_category=1,
            received_on='2021-01-01T00:00',
            details='Test Details',
            created_by=self.user
        )

    def test_action_form(self):
        form = ActionForm({
            'incident': 1,
            'action_code': 1,
            'details': 'Test Details',
        })
        self.assertTrue(form.is_valid(), msg=form.errors)

    def test_action_form_date(self):
        form = ActionForm({
            'incident': 1,
            'action_code': 1,
            'details': 'Test Details',
            'completed_on': '2021-01-01T00:00',
        })
        self.assertTrue(form.is_valid(), msg=form.errors)
    
    def test_action_form_invalid(self):
        form = ActionForm({
            'incident': 1,
            'action_code': 'q',
            'completed_on': 'fsdfsf',
        })
        self.assertFalse(form.is_valid(), msg=form.errors)
        self.assertEqual(form.errors['details'], ['This field is required.'])

