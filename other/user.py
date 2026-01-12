from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.cache import cache
from django.core.validators import URLValidator
from .Social_Model import SocialModel
import jwt
from datetime import datetime, timedelta
from django.conf import settings

class UserManager(BaseUserManager):
    """Custom user manager for UserModel"""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)

class UserModel(AbstractBaseUser, PermissionsMixin):
    # Authentication fields
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True)
    
    # Personal information
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True)
    timezone = models.CharField(max_length=50, default='UTC')
    
    # Social links
    social_links = models.ManyToManyField(SocialModel, blank=True, related_name='users')
    
    # Status fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    failed_login_attempts = models.IntegerField(default=0)
    last_password_change = models.DateTimeField(auto_now_add=True)
    account_locked_until = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'
        db_table_comment = 'User model for portfolio site owner'
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['username']),
        ]

    def __str__(self):
        return self.email

    def get_full_name(self):
        """Return the full name of the user"""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """Return the short name of the user"""
        return self.first_name

    def get_profile_completion_percentage(self):
        """Calculate the profile completion percentage"""
        fields = ['email', 'username', 'first_name', 'last_name', 'bio', 
                 'profile_picture', 'location', 'timezone']
        filled_fields = sum(1 for field in fields if getattr(self, field))
        return (filled_fields / len(fields)) * 100

    def validate_profile_picture(self):
        """Validate the profile picture URL"""
        if self.profile_picture:
            validator = URLValidator()
            try:
                validator(self.profile_picture)
                return True
            except:
                return False
        return True

    def generate_email_verification_token(self):
        """Generate token for email verification"""
        token = jwt.encode({
            'user_id': self.id,
            'exp': datetime.utcnow() + timedelta(days=1),
            'type': 'email_verification'
        }, settings.SECRET_KEY, algorithm='HS256')
        return token

    def generate_password_reset_token(self):
        """Generate token for password reset"""
        token = jwt.encode({
            'user_id': self.id,
            'exp': datetime.utcnow() + timedelta(hours=1),
            'type': 'password_reset'
        }, settings.SECRET_KEY, algorithm='HS256')
        return token

    def track_login_attempt(self, success):
        """Track login attempts and handle account locking"""
        if success:
            self.failed_login_attempts = 0
            self.account_locked_until = None
        else:
            self.failed_login_attempts += 1
            if self.failed_login_attempts >= 5:
                self.account_locked_until = timezone.now() + timedelta(minutes=30)
        self.save()

    def is_account_locked(self):
        """Check if the account is locked"""
        if self.account_locked_until and self.account_locked_until > timezone.now():
            return True
        return False

    def get_cached_profile(self):
        """Get cached user profile data"""
        cache_key = f'user_profile_{self.id}'
        profile = cache.get(cache_key)
        if profile is None:
            profile = {
                'id': self.id,
                'email': self.email,
                'username': self.username,
                'full_name': self.get_full_name(),
                'bio': self.bio,
                'profile_picture': self.profile_picture,
                'location': self.location,
                'social_links': list(self.social_links.values('platform', 'url'))
            }
            cache.set(cache_key, profile, timeout=3600)  # Cache for 1 hour
        return profile

    def clear_profile_cache(self):
        """Clear the cached profile data"""
        cache_key = f'user_profile_{self.id}'
        cache.delete(cache_key)

    def save(self, *args, **kwargs):
        """Override save method to handle cache and validations"""
        # Clear cache on save
        if self.pk:
            self.clear_profile_cache()
        
        # Validate profile picture URL
        if not self.validate_profile_picture():
            raise ValueError(_('Invalid profile picture URL'))
            
        super().save(*args, **kwargs)