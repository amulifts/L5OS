# opencanary_configurator/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import HoneypotService
import json
import subprocess

@receiver(post_save, sender=HoneypotService)
def update_opencanary_config(sender, instance, **kwargs):
    if instance.service_type == 'http' or instance.service_type == 'https':
        # Path to the OpenCanary configuration file
        config_file_path = '/etc/opencanaryd/opencanary.conf'
        
        # Read the contents of the configuration file
        with open(config_file_path, 'r') as config_file:
            config_data = json.load(config_file)
        
        # Enable HTTP or HTTPS service in the configuration based on service_type
        if instance.service_type == 'http':
            config_data['http.enabled'] = instance.is_enabled
        elif instance.service_type == 'https':
            config_data['https.enabled'] = instance.is_enabled
        
        # Write the modified configuration back to the file
        with open(config_file_path, 'w') as config_file:
            json.dump(config_data, config_file, indent=4)

        # Check the HTTP service state
        if instance.is_enabled:
            # Start the opencanary service
            subprocess.run(['sudo', 'opencanaryd', '--start'])
        else:
            # Stop the opencanary service
            subprocess.run(['sudo', 'opencanaryd', '--stop'])

        # Restart the opencanary service
        subprocess.run(['sudo', 'opencanaryd', '--restart'])