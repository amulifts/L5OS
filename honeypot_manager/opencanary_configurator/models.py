# opencanary_configurator/models.py

from django.db import models
from datetime import datetime

class HoneypotService(models.Model):
    SERVICE_CHOICES = [
        ('http', 'HTTP'),
        ('https', 'HTTPS'),
        # Add more services as needed
    ]
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    is_enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.service_type
    
