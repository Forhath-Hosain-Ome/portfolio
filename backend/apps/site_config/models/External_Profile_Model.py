from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class ExternalProfileModel(TimeStampedModel, OrderableModel):
    """External portfolio profiles (Dribbble, Behance, etc.)."""
    
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    icon_name = models.CharField(max_length=50)
    primary_color = models.CharField(max_length=20, default='#000000')
    cta_text = models.CharField(max_length=50, default='View Profile')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
        indexes = [
            models.Index(fields=["is_active"]),
        ]
    
    def __str__(self):
        return f"{self.platform_name} - {self.title}"
