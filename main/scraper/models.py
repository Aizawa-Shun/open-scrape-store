from django.db import models

class WebData(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    images = models.TextField(blank=True)