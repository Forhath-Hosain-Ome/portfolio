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
