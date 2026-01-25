from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel

class SkillModel(TimeStampedModel, OrderableModel):
    """Skill model."""
    
    SKILL_CATEGORIES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('design', 'Design'),
        ('tools', 'Tools'),
        ('soft', 'Soft Skills'),
    )
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    
    # Icon
    icon_name = models.CharField(
        max_length=50,
        blank=True,
        help_text="Icon class name"
    )
    
    # Proficiency
    proficiency_percent = models.PositiveIntegerField(
        default=50,
        help_text="Proficiency level (0-100)"
    )
    
    # Content
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['category', 'display_order']
        indexes = [
            models.Index(fields=["category"]),
        ]
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"