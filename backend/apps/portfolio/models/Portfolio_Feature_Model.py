
from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel, PublishableModel, OrderableModel, SEOModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class PortfolioFeatureModel(OrderableModel):
    """Features/highlights for portfolio items."""
    
    portfolio_item = models.ForeignKey(
        PortfolioItem,
        on_delete=models.CASCADE,
        related_name='features'
    )
    feature_text = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.feature_text

