from django.db import models
from django.utils.translation import gettext_lazy as _

class PublishableModel(models.Model):
    """Abstract base model for publishable content."""
    published = models.BooleanField(_("Published"), default=False)
    published_at = models.DateTimeField(_("Published at"), null=True, blank=True)

    class Meta:
        abstract = True