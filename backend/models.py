# ============================================================================
# apps/core/models.py - Abstract Base Models
# ============================================================================

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """Abstract base model with created and updated timestamps."""
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        abstract = True


class PublishableModel(models.Model):
    """Abstract base model for publishable content."""
    published = models.BooleanField(_("Published"), default=False)
    published_at = models.DateTimeField(_("Published at"), null=True, blank=True)

    class Meta:
        abstract = True


class OrderableModel(models.Model):
    """Abstract base model for orderable items."""
    display_order = models.PositiveIntegerField(_("Display order"), default=0)

    class Meta:
        abstract = True
        ordering = ['display_order']


class SEOModel(models.Model):
    """Abstract base model for SEO fields."""
    meta_title = models.CharField(_("Meta title"), max_length=60, blank=True)
    meta_description = models.TextField(_("Meta description"), max_length=160, blank=True)
    meta_keywords = models.CharField(_("Meta keywords"), max_length=255, blank=True)

    class Meta:
        abstract = True


# ============================================================================
# apps/site_config/models.py
# ============================================================================

from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel


class SiteSetting(models.Model):
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


class ContactInfo(TimeStampedModel, OrderableModel):
    """Contact information model."""
    
    INFO_TYPES = (
        ('address', 'Address'),
        ('phone', 'Phone'),
        ('email', 'Email'),
        ('social', 'Social Media'),
    )
    
    info_type = models.CharField(max_length=20, choices=INFO_TYPES)
    icon_name = models.CharField(max_length=50)
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    link_url = models.CharField(max_length=200, blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
        verbose_name_plural = "Contact information"
    
    def __str__(self):
        return f"{self.get_info_type_display()}: {self.value}"


class SocialLink(TimeStampedModel, OrderableModel):
    """Social media links model."""
    
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()
    icon_name = models.CharField(max_length=50)
    display_color = models.CharField(max_length=20, default='#000000')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.platform_name


class ExternalProfile(TimeStampedModel, OrderableModel):
    """External portfolio profiles (Dribbble, Behance, etc.)."""
    
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField()
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, blank=True)
    icon_name = models.CharField(max_length=50)
    primary_color = models.CharField(max_length=20, default='#000000')
    cta_text = models.CharField(max_length=50, default='View Profile')
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.platform_name} - {self.title}"


class Partner(TimeStampedModel, OrderableModel):
    """Partners/clients model."""
    
    partner_name = models.CharField(max_length=100)
    logo_default = models.ImageField(upload_to='partners/')
    logo_hover = models.ImageField(upload_to='partners/', blank=True)
    website_url = models.URLField(blank=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.partner_name


class FunFact(TimeStampedModel, OrderableModel):
    """Statistics/fun facts model."""
    
    icon_name = models.CharField(max_length=50)
    count_value = models.PositiveIntegerField()
    label = models.CharField(max_length=100)
    count_suffix = models.CharField(max_length=10, blank=True, help_text="e.g., '+', 'K', 'M'")
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.label}: {self.count_value}"


class PricingPlan(TimeStampedModel, OrderableModel):
    """Pricing plans model."""
    
    plan_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    billing_period = models.CharField(
        max_length=20,
        choices=[
            ('monthly', 'Monthly'),
            ('yearly', 'Yearly'),
            ('one-time', 'One-time'),
        ],
        default='monthly'
    )
    description = models.TextField(blank=True)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Styling
    bg_color = models.CharField(max_length=20, default='#ffffff')
    text_color = models.CharField(max_length=20, default='#000000')
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.plan_name} - {self.currency}{self.price}/{self.billing_period}"


class PlanFeature(OrderableModel):
    """Features for pricing plans."""
    
    plan = models.ForeignKey(
        PricingPlan,
        on_delete=models.CASCADE,
        related_name='features'
    )
    feature_text = models.CharField(max_length=200)
    is_included = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        status = "✓" if self.is_included else "✗"
        return f"{status} {self.feature_text}"