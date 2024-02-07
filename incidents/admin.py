from django.contrib import admin
from .models import Incident, Action

# Register your models here.

admin.site.register(Incident)
admin.site.register(Action)
