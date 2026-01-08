from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class ContactInfoModels(TimeStampedModel, OrderableModel):
    """Contact information model."""
    
    INFO_TYPES = (
        ('address', 'Address'),
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('social', 'Social Media'),
    )
    
    info_type = models.CharField(max_length=20, choices=INFO_TYPES)
    icon_name = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    link_url = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
        verbose_name_plural = "Contact information"
    
    def __str__(self):
        return f"{self.get_info_type_display()}: {self.value}"
