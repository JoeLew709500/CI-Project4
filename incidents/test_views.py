from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Incident, Action

class TestIncidentViews(TestCase):
    """
    Test the views for the incidents app
    """
    def set_up(self):
        """
        Set up user,incident and action
        """
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
        """
        Test the index view
        """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/index.html')

    def test_incident_list_view(self):
        """
        Test the incident list view
        """
        response = self.client.get(reverse('incident_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/incident_list.html')

    def test_incident_detail_view(self):
        """
        Test the incident detail view
        """
        response = self.client.get(reverse('incident_detail', args=[self.incident.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/incident.html')

    def test_incident_create_view(self):
        """
        Test the incident create view
        """
        response = self.client.get(reverse('incident_new'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/incident.html')

    def test_action_create_view(self):
        """
        Test the action create view
        """
        response = self.client.get(reverse('action_new', args=[self.incident.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/action_detail.html')

    def test_photos_view(self):
        """
        Test the photos view
        """
        response = self.client.get(reverse('photos', args=[self.incident.id, self.action.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'incidents/action_photos.html')
