from django.db import models
from apps.core.models import OrderableModel
from apps.portfolio.models import PortfolioItemModel

class PortfolioFeatureModel(OrderableModel):
    """Features/highlights for portfolio items."""
    
    portfolio_item = models.ForeignKey(
        PortfolioItemModel,
        on_delete=models.CASCADE,
        related_name='features'
    )
    feature_text = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.feature_text

