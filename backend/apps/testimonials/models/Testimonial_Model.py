from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel


class TestimonialModel(TimeStampedModel, OrderableModel):
    """Testimonial model."""
    
    # Client info
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100, blank=True)
    client_image = models.ImageField(upload_to='testimonials/')
    
    # Content
    testimonial_text = models.TextField()
    
    # Rating
    rating = models.PositiveIntegerField(
        default=5,
        choices=[(i, i) for i in range(1, 6)]
    )
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Project reference (optional)
    related_project = models.ForeignKey(
        'portfolio.PortfolioItemModel',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='testimonials'
    )
    
    class Meta:
        ordering = ['-is_featured', 'display_order']
        indexes = [
            models.Index(fields=["is_active", "rating", "is_featured"]),
        ]
    
    def __str__(self):
        return f"{self.client_name} - {self.client_company}"
