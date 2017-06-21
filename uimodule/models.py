from django.db import models
from django.utils import timezone

# Create your models here.
class Satellite(models.Model):
    title = models.CharField(max_length = 200)
    gyroX = models.CharField(max_length = 10)
    gyroY = models.CharField(max_length = 10)
    gyroZ = models.CharField(max_length = 10)
    gpsLat = models.CharField(max_length = 10)
    gpsLon = models.CharField(max_length = 10)
    updated_time = models.DateTimeField(default = timezone.now)
