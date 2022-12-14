# Django
from email.policy import default
from django.db import models

# Customize
from storages.models import Storage

class Sensor(models.Model):
    sensor_x = models.IntegerField()
    sensor_y = models.IntegerField()
    sensor_z = models.IntegerField()
    sensor_temperature = models.FloatField()
    sensor_code = models.IntegerField(default = 0)
    sensor_category = models.CharField(max_length = 3, default = "001") 
    # 001 is code which is identify for sensor of temperatures
    sensor_storage = models.ForeignKey(Storage, on_delete=models.CASCADE, related_name="sensors")

    def __str__(self) -> str:
        return str(self.id) + "_Kho lanh " + str(self.sensor_storage.id)