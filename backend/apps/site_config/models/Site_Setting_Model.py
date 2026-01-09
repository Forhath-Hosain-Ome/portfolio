from django.db import models


class SiteSettingModel(models.Model):
    """Site-wide settings model."""
    
    SETTING_TYPES = (
        ('text', 'Text'),
        ('textarea', 'Textarea'),
        ('number', 'Number'),
        ('boolean', 'Boolean'),
        ('json', 'JSON'),
    )
    
    SETTING_GROUPS = (
        ('general', 'General'),
        ('seo', 'SEO'),
        ('social', 'Social Media'),
        ('contact', 'Contact'),
        ('analytics', 'Analytics'),
    )
    
    setting_key = models.CharField(max_length=100, unique=True)
    setting_value = models.TextField()
    setting_type = models.CharField(max_length=20, choices=SETTING_TYPES, default='text')
    setting_group = models.CharField(max_length=20, choices=SETTING_GROUPS, default='general')
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['setting_group', 'setting_key']
    
    def __str__(self):
        return f"{self.setting_key} ({self.get_setting_group_display()})"
