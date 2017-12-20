from django.db import models 
from django.conf import settings
from django.utils import timezone

class Elvis(models.Model): 
# https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#referencing-the-user-model
    current_user = models.ForeignKey(
       settings.AUTH_USER_MODEL,
       on_delete=models.CASCADE,
       null=True,
       default=None,
       blank=True
    )
    name = models.CharField(max_length=20)
    revision = models.CharField(max_length=20)
    has_display = models.BooleanField()
    ip_address = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    device_id = models.CharField(max_length=20)
    firmware = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    
    IN_USE = 'in_use'  
    OFFLINE = 'offline'
    AVAILABLE = 'available'
    
    AVAILABILITY_CHOICES = (
        (IN_USE, 'In Use'),
        (OFFLINE, 'Offline'),
        (AVAILABLE, 'Available'),
    )
    availability = models.CharField(
        max_length = 15,
        choices=AVAILABILITY_CHOICES,
        default=AVAILABLE,
    )
    
    def __str__(self):
        return self.name
    
    