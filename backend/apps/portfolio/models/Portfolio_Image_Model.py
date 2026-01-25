from django.db import models
from apps.core.models import OrderableModel, TimeStampedModel
from .Portfolio_Item_Model import PortfolioItemModel

class PortfolioImageModel(OrderableModel, TimeStampedModel):
    """Additional images for portfolio items."""
    
    portfolio_item = models.ForeignKey(
        PortfolioItemModel,
        on_delete=models.CASCADE,
        related_name='additional_images'
    )
    image = models.ImageField(upload_to='portfolio/%Y/%m/gallery/')
    caption = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['display_order']
        indexes = [
            models.Index(fields=["is_primary"]),
        ]
    
    def __str__(self):
        return f"{self.portfolio_item.title} - Image {self.display_order}"