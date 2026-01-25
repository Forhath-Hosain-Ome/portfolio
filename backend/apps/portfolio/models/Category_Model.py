from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel


class CategoryModel(TimeStampedModel):
    """Category model for portfolio items, blog posts, etc."""
    
    CATEGORY_TYPES = (
        ('portfolio', 'Portfolio'),
        ('blog', 'Blog'),
        ('service', 'Service'),
    )
    
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    type = models.CharField(max_length=20, choices=CATEGORY_TYPES)
    description = models.TextField(blank=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        indexes = [
            models.Index(fields=["name", "type", "parent"]),
        ]