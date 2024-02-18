from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Incident, Action, ActionPhoto
from .forms import IncidentForm, ActionForm, ActionFormNew, IncidentFormSearch

class TestIncidentViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword',
            email='test@test.com'
        )

        self.incident = Incident.objects.create(
            location='Test Location',
            incident_category=1,
            received_on='2021-01-01T00:00',
            details='Test Details',
            created_by=self.user
        )

        self.action = Action.objects.create(
            incident=self.incident,
            action_code=1,
            details='Test Details',
            completed_on='2021-01-01T00:00',
            created_by=self.user
        )

    def test_index_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/index.html')

    def test_incident_list_view(self):
        response = self.client.get(reverse('incident_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/incident_list.html')

    def test_incident_detail_view(self):
        response = self.client.get(reverse('incident_detail', args=[self.incident.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/incident.html')

    def test_incident_create_view(self):
        response = self.client.get(reverse('incident_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/incident.html')

    def test_action_create_view(self):
        response = self.client.get(reverse('action_new', args=[self.incident.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/action_detail.html')
