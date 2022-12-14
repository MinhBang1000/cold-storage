from email.policy import default
from django.db import models
from storages.models import Storage

# Create your models here.
class Pallet(models.Model):
    pallet_length = models.IntegerField()
    pallet_width = models.IntegerField()
    pallet_height = models.IntegerField()
    pallet_drawers = models.IntegerField()  
    pallet_active = models.BooleanField(default = False)
    pallet_color = models.CharField(max_length = 250, default = "NONE")
    pallet_storage = models.ForeignKey(Storage, on_delete = models.CASCADE, related_name = "storage_pallets")