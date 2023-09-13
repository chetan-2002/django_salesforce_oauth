from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class SalesforceToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    access_token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    instance_url = models.URLField()

    def __str__(self):
        return f"Salesforce Token - {self.access_token}"