from django.db import models
from ._Core_Model import BaseModel


class SocialModel(BaseModel):
    """Model to store social media links for the portfolio"""
    
    # Social media platforms
    PLATFORM_CHOICES = [
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
        ('twitter', 'Twitter'),
        ('linkedin', 'LinkedIn'),
        ('github', 'GitHub'),
        ('youtube', 'YouTube'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
        ('portfolio', 'Portfolio'),
        ('other', 'Other'),
    ]
    
    platform = models.CharField(
        max_length=20,
        choices=PLATFORM_CHOICES,
        unique=True,
        help_text="Select the social media platform"
    )
    url = models.URLField(
        help_text="Enter the URL or contact information"
    )
    display_name = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional display name (e.g., @username)"
    )
    icon_class = models.CharField(
        max_length=100,
        blank=True,
        help_text="CSS class for icon (e.g., fab fa-facebook)"
    )
    order = models.PositiveIntegerField(
        default=0,
        help_text="Order of display on portfolio"
    )
    
    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
        ordering = ['order']
    
    def __str__(self):
        platform_display = dict(self.PLATFORM_CHOICES).get(self.platform, self.platform)
        return f"{platform_display} - {self.display_name or self.url}"
