from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel, PublishableModel, OrderableModel, SEOModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class TagModel(TimeStampedModel):
    """Tag model for cross-referencing content."""
    
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

