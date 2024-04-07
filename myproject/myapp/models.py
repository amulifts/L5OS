from django.db import models
from django.utils import timezone

class LoginAttempt(models.Model):
    ip_address = models.CharField(max_length=45)  # Updated to accommodate IPv6 addresses
    timestamp = models.DateTimeField(auto_now_add=True)
    browser = models.CharField(max_length=100, blank=True, null=True)
    platform = models.CharField(max_length=100, blank=True, null=True)
    isp = models.CharField(max_length=200, blank=True, null=True)
    user_agent = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    referring_url = models.URLField(max_length=200, blank=True, null=True)
    latitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    longitude = models.DecimalField(max_digits=30, decimal_places=15, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    timezone = models.CharField(max_length=100, blank=True, null=True)

    name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    passphrase = models.CharField(max_length=80, blank=True, null=True)
    request_type = models.CharField(max_length=4, blank=True, null=True)  # To store 'GET' or 'POST'

    def __str__(self):
        local_time = timezone.localtime(self.timestamp)
        # return f"Attempt from IP {self.ip_address} at {local_time.strftime('%Y-%m-%d %I:%M:%S %p')}"
        return f"{self.request_type} request from IP {self.ip_address} at {local_time.strftime('%Y-%m-%d %I:%M:%S %p')}"


