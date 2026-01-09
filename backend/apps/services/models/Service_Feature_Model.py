from django.db import models
from apps.core.models import OrderableModel
from apps.services.models import ServiceModel


class ServiceFeatureModel(OrderableModel):
    """Features for services."""
    
    service = models.ForeignKey(
        ServiceModel,
        on_delete=models.CASCADE,
        related_name='features'
    )
    feature_text = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.service.title} - {self.feature_text}"