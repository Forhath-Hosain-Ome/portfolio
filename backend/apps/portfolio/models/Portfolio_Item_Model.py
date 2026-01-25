from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel, PublishableModel, OrderableModel, SEOModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .Category_Model import CategoryModel
from .Tag_Model import TagModel

class PortfolioItemModel(TimeStampedModel, PublishableModel, OrderableModel, SEOModel):
    """Portfolio item model."""
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    # Images
    main_image = models.ImageField(upload_to='portfolio/%Y/%m/')
    thumbnail = ImageSpecField(
        source='main_image',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 85}
    )
    
    # Content
    short_description = models.TextField(max_length=500)
    description = models.TextField()
    description_extended = models.TextField(blank=True)
    
    # Additional info
    client_name = models.CharField(max_length=100, blank=True)
    project_url = models.URLField(blank=True)
    project_date = models.DateField()
    
    # Engagement metrics
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    
    # Relationships
    categories = models.ManyToManyField(
        CategoryModel,
        related_name='portfolio_items',
        limit_choices_to={'type': 'portfolio'}
    )
    tags = models.ManyToManyField(TagModel, related_name='portfolio_items', blank=True)
    
    class Meta:
        ordering = ['-published_at', 'display_order']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=["title"]),
        ]