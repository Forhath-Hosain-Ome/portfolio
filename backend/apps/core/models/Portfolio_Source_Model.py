from django.db import models
from django.contrib.auth.models import User
from .Time_Stamped_Model import TimeStampedModel

class PortfolioSourceModel(TimeStampedModel):
    domain = models.CharField(max_length=255)
    user_domain = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['domain']
        indexes = [
            models.Index(fields=["domain", "user_domain"]),
        ]
    
    def __str__(self):
        return self.domain