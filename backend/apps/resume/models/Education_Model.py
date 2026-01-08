from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class EducationModel(TimeStampedModel, OrderableModel):
    """Education model."""
    
    degree_title = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    
    # Dates
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    
    # Content
    description = models.TextField(blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    
    # Media
    institution_logo = models.ImageField(upload_to='education/', blank=True)
    
    class Meta:
        ordering = ['-start_date', 'display_order']
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree_title} - {self.institution}"
