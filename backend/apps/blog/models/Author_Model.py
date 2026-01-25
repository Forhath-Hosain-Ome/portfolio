from django.db import models
from django.contrib.auth.models import User
from apps.core.models import TimeStampedModel


class AuthorModel(TimeStampedModel):
    """Author profile model."""
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='author_profile')
    display_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='authors/', blank=True)
    website = models.URLField(blank=True)
    
    # Social links
    twitter = models.CharField(max_length=100, blank=True)
    linkedin = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    
    class Meta:
        ordering = ['display_name']
        indexes = [
            models.Index(fields=["user", "display_name"]),
        ]
    
    def __str__(self):
        return self.display_name