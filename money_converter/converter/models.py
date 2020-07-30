from django.db import models

# Create your models here.
class Converter(models.Model):
    originalText = models.CharField(max_length=255)
    convertedText = models.CharField(max_length=255)