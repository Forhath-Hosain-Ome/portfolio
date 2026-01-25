from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class PartnerModel(TimeStampedModel, OrderableModel):
    """Partners/clients model."""
    
    partner_name = models.CharField(max_length=100)
    logo_default = models.ImageField(upload_to='partners/')
    logo_hover = models.ImageField(upload_to='partners/', blank=True)
    website_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
        indexes = [
            models.Index(fields=["is_active"]),
        ]
    
    def __str__(self):
        return self.partner_name