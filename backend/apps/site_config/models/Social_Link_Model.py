from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class SocialLinkModel(TimeStampedModel, OrderableModel):
    """Social media links model."""
    
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()
    icon_name = models.CharField(max_length=50)
    display_color = models.CharField(max_length=20, default='#000000')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
        indexes = [
            models.Index(fields=["is_active"]),
        ]
    
    def __str__(self):
        return self.platform_name
