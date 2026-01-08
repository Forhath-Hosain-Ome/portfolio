
from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel


class ServiceModel(TimeStampedModel, OrderableModel):
    """Service model."""
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    # Icon
    icon_name = models.CharField(
        max_length=50,
        help_text="Icon class name (e.g., 'fa-code', 'ri-palette-line')"
    )
    
    # Content
    short_description = models.TextField(max_length=200)
    full_description = models.TextField()
    
    # Styling
    bg_color = models.CharField(max_length=20, default='#ffffff')
    text_color = models.CharField(max_length=20, default='#000000')
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)