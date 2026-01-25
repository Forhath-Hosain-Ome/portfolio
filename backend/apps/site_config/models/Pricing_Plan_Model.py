from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class PricingPlanModel(TimeStampedModel, OrderableModel):
    """Pricing plans model."""
    
    plan_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    billing_period = models.CharField(
        max_length=20,
        choices=[
            ('monthly', 'Monthly'),
            ('yearly', 'Yearly'),
            ('one-time', 'One-time'),
        ],
        default='monthly'
    )
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Styling
    bg_color = models.CharField(max_length=20, default='#ffffff')
    text_color = models.CharField(max_length=20, default='#000000')
    
    class Meta:
        ordering = ['display_order']
        indexes = [
            models.Index(fields=["is_active","is_featured"]),
        ]
    
    def __str__(self):
        return f"{self.plan_name} - {self.currency}{self.price}/{self.billing_period}"
