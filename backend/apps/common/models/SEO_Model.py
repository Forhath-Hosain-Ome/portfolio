from django.db import models
from django.utils.translation import gettext_lazy as _

class SEOModel(models.Model):
    """Abstract base model for SEO fields."""
    meta_title = models.CharField(_("Meta title"), max_length=60, blank=True)
    meta_description = models.TextField(_("Meta description"), max_length=160, blank=True)
    meta_keywords = models.CharField(_("Meta keywords"), max_length=255, blank=True)

    class Meta:
        abstract = True