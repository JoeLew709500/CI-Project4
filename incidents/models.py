from django.db import models
from django.contrib.auth.models import User


INCIDENT_CATEGORY_CHOICES = (
    (1, 'Fly Tipping'),
    (2, 'Noise Pollution'),
    (3, 'Abandoned Vehicle'),
    (4, 'Littering'),
    (5, 'Statutory Nuisance (e.g. odour, light, etc.)'),
    (6, 'Presentation of Waste (Domestic)'),
    (7, 'Presentation of Waste (Commercial)'),
    (8, 'Atmospheric Pollution (e.g. smoke, fumes, etc.)'),
    (9, 'Accumulation of Waste'),
    (10, 'Trade Waste Checking'),
    (11, 'ASB (Anti-Social Behaviour)'),
    )


ACTION_CODES = (
    (1, 'Visit to site'),
    (2, 'Notice Issued'),
    (3, 'General File Note'),
    (4, 'Referral'),
    (5, 'Out going communication (e.g. letter, email, etc.)'),
    (6, 'Enforcement action taken'),
)


# Create your models here.
class Incident(models.Model):
    location = models.CharField(max_length=200)
    incident_category = models.IntegerField(choices=INCIDENT_CATEGORY_CHOICES)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='incidents')
    received_on = models.DateTimeField()
    details = models.TextField()
    closed_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
            return self.get_incident_category_display()
    
    
class Action(models.Model):
    incident = models.ForeignKey(Incident,on_delete=models.CASCADE, 
                                related_name='actions')
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='actions')
    action_code = models.IntegerField(choices=ACTION_CODES)
    details = models.TextField()
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.get_action_code_display()
    
