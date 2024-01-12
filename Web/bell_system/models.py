from django.db import models

# Create your models here.
# bell_system/models.py

from django.db import models

class BusRoute(models.Model):
    route_number = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return self.route_number

class BusStop(models.Model):
    route = models.ForeignKey(BusRoute, related_name='bus_stops', on_delete=models.CASCADE)
    stop_name = models.CharField(max_length=100)

    def __str__(self):
        return self.stop_name
