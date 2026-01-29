from django.db import models
from apps.core.models import OrderableModel, TimeStampedModel
from .Portfolio_Item_Model import PortfolioItemModel

class PortfolioFeatureModel(OrderableModel, TimeStampedModel):
    """Features/highlights for portfolio items."""
    SKILLS_TYPES = (
        ('seo', 'SEO EXPERT'),
        ('full stack developer', 'Full Stack Developer'),
        ('web developer', 'WEB DEVELOPER'),
        ('cyber security expert', 'CYBER SECURITY EXPERT'),
    )

    portfolio_item = models.ForeignKey(
        PortfolioItemModel,
        on_delete=models.CASCADE,
        related_name='features'
    )

    greet_message = models.CharField(max_length=30)

    feature_skill = models.CharField(max_length=30, choices=SKILLS_TYPES)

    feature_text = models.CharField(max_length=200)
    feature_text2 = models.CharField(max_length=200)

    resume = models.FileField(upload_to='portfolio/%Y/%m/resume/', null = True, blank = True)
    
    class Meta:
        ordering = ['display_order']
        indexes = [
            models.Index(fields=["portfolio_item"]),
        ]
    
    def __str__(self):
        return self.feature_text