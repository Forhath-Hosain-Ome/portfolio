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
# apps/portfolio/models.py
# ============================================================================

# ============================================================================
# apps/blog/models.py
# ============================================================================

from django.db import models
from django.contrib.auth.models import User
from apps.core.models import TimeStampedModel, PublishableModel, SEOModel
from apps.portfolio.models import Category, Tag
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Author(TimeStampedModel):
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
    
    def __str__(self):
        return self.display_name


class BlogPost(TimeStampedModel, PublishableModel, SEOModel):
    """Blog post model."""
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    
    # Author
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    
    # Images
    featured_image = models.ImageField(upload_to='blog/%Y/%m/')
    thumbnail = ImageSpecField(
        source='featured_image',
        processors=[ResizeToFill(400, 300)],
        format='JPEG',
        options={'quality': 85}
    )
    
    # Content
    excerpt = models.TextField(max_length=300)
    content = models.TextField()
    content_extended = models.TextField(blank=True)
    
    # Reading time
    read_time_minutes = models.PositiveIntegerField(default=5)
    
    # Engagement metrics
    views_count = models.PositiveIntegerField(default=0)
    likes_count = models.PositiveIntegerField(default=0)
    comments_count = models.PositiveIntegerField(default=0)
    
    # Featured
    is_featured = models.BooleanField(default=False)
    
    # Relationships
    categories = models.ManyToManyField(
        Category,
        related_name='blog_posts',
        limit_choices_to={'type': 'blog'}
    )
    tags = models.ManyToManyField(Tag, related_name='blog_posts', blank=True)
    
    class Meta:
        ordering = ['-published_at']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# ============================================================================
# apps/services/models.py
# ============================================================================

from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel


class Service(TimeStampedModel, OrderableModel):
    """Service model."""
    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    
    # Icon
    icon_name = models.CharField(
        max_length=50,
        help_text="Icon class name (e.g., 'fa-code', 'ri-palette-line')"
    )
    
    # Content
    short_description = models.TextField(max_length=200)
    full_description = models.TextField()
    
    # Styling
    bg_color = models.CharField(max_length=20, default='#ffffff')
    text_color = models.CharField(max_length=20, default='#000000')
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class ServiceFeature(OrderableModel):
    """Features for services."""
    
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='features'
    )
    feature_text = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['display_order']
    
    def __str__(self):
        return f"{self.service.title} - {self.feature_text}"


# ============================================================================
# apps/resume/models.py
# ============================================================================

from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel


class WorkExperience(TimeStampedModel, OrderableModel):
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
    
    def __str__(self):
        return f"{self.job_title} at {self.company_name}"


class Education(TimeStampedModel, OrderableModel):
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


class Skill(TimeStampedModel, OrderableModel):
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
    
    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


# ============================================================================
# apps/testimonials/models.py
# ============================================================================

from django.db import models
from apps.core.models import TimeStampedModel, OrderableModel


class Testimonial(TimeStampedModel, OrderableModel):
    """Testimonial model."""
    
    # Client info
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100, blank=True)
    client_image = models.ImageField(upload_to='testimonials/')
    
    # Content
    testimonial_text = models.TextField()
    
    # Rating
    rating = models.PositiveIntegerField(
        default=5,
        choices=[(i, i) for i in range(1, 6)]
    )
    
    # Status
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    # Project reference (optional)
    related_project = models.ForeignKey(
        'portfolio.PortfolioItem',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='testimonials'
    )
    
    class Meta:
        ordering = ['-is_featured', 'display_order']
    
    def __str__(self):
        return f"{self.client_name} - {self.client_company}"


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