from django.db import models
from django.core.validators import URLValidator
from .Social_Model import SocialModel
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    # Basic Information
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="e.g., Full Stack Developer, UI/UX Designer")
    bio = models.TextField(help_text="A brief introduction about yourself")
    
    # Contact Information
    email = models.EmailField(help_text="Professional email address")
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, help_text="City, Country")
    
    # Media
    profile_picture = models.URLField(null=True, blank=True)
    # resume = models.URLField(null=True, blank=True, help_text="Link to your resume/CV")
    
    # Professional Summary
    # years_of_experience = models.PositiveIntegerField(default=0)
    # professional_summary = models.TextField(help_text="Detailed professional background and expertise")
    
    # Social Links (One-to-Many relationship as portfolio owner can have multiple social links)
    social_links = models.ForeignKey(SocialModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='portfolio_owner')
    
    # Additional Information
    available_for_hire = models.BooleanField(default=True)
    preferred_work_type = models.CharField(
        max_length=50,
        choices=[
            ('full_time', 'Full Time'),
            ('part_time', 'Part Time'),
            ('contract', 'Contract'),
            ('freelance', 'Freelance'),
        ],
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Portfolio Owner'
        verbose_name_plural = 'Portfolio Owner'
        db_table = 'portfolio_owner'
        # db_table_comment = 'Information about the portfolio owner'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

    def validate_profile_picture(self):
        if self.profile_picture:
            validator = URLValidator()
            try:
                validator(self.profile_picture)
                return True
            except:
                return False
        return True

    # def validate_resume_url(self):
    #     """Validate the resume URL"""
    #     if self.resume:
    #         validator = URLValidator()
    #         try:
    #             validator(self.resume)
    #             return True
    #         except:
    #             return False
    #     return True

    def save(self, *args, **kwargs):
        """Override save method to handle validations"""
        if not self.validate_profile_picture():
            raise ValueError('Invalid profile picture URL')
        # if not self.validate_resume_url():
        #     raise ValueError('Invalid resume URL')
        super().save(*args, **kwargs)