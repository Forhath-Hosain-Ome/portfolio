from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class FunFactModel(TimeStampedModel, OrderableModel):
    """Statistics/fun facts model."""
    
    icon_name = models.CharField(max_length=50)
    count_value = models.PositiveIntegerField()
    label = models.CharField(max_length=100)
    count_suffix = models.CharField(max_length=10, blank=True, help_text="e.g., '+', 'K', 'M'")
    
    class Meta:
        ordering = ['display_order']
        indexes = [
            models.Index(fields=["is_active"]),
        ]
    
    def __str__(self):
        return f"{self.label}: {self.count_value}"
