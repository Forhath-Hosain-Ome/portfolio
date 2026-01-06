from django.db import models
from django.utils.translation import gettext_lazy as _

class OrderableModel(models.Model):
    """Abstract base model for orderable items."""
    display_order = models.PositiveIntegerField(_("Display order"), default=0)

    class Meta:
        abstract = True
        ordering = ['display_order']