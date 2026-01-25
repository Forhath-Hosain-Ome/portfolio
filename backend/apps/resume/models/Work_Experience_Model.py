from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel


class WorkExperienceModel(TimeStampedModel, OrderableModel):
    """Work experience model."""
    
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    
    # Dates
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    
    # Content
    description = models.TextField()
    
    # Media
    company_logo = models.ImageField(upload_to='experience/', blank=True)
    company_website = models.URLField(blank=True)
    
    class Meta:
        ordering = ['-start_date', 'display_order']
        verbose_name_plural = "Work experiences"
        indexes = [
            models.Index(fields=["is_current"]),
        ]
    
    def __str__(self):
        return f"{self.job_title} at {self.company_name}"