from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class PlanFeatureModel(OrderableModel):
    """Features for pricing plans."""
    
    plan = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        related_name='features'
    )
    feature_text = models.CharField(max_length=200)
    is_included = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        status = "✓" if self.is_included else "✗"
        return f"{status} {self.feature_text}"