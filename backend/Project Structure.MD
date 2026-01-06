"""
Django Portfolio Backend - Complete Project Structure
=====================================================

portfolio_backend/
│
├── manage.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
│
├── config/                          # Project configuration
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py                  # Base settings
│   │   ├── development.py           # Dev settings
│   │   ├── production.py            # Prod settings
│   │   └── testing.py               # Test settings
│   ├── urls.py                      # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── apps/                            # Django apps
│   │
│   ├── portfolio/                   # Portfolio app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   ├── filters.py
│   │   ├── permissions.py
│   │   └── tests/
│   │       ├── test_models.py
│   │       ├── test_views.py
│   │       └── test_serializers.py
│   │
│   ├── blog/                        # Blog app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── admin.py
│   │   └── tests/
│   │
│   ├── services/                    # Services app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── resume/                      # Resume/About app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── testimonials/                # Testimonials app
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   ├── site_config/                 # Site configuration
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── admin.py
│   │
│   └── common/                      # Shared utilities
│       ├── __init__.py
│       ├── models.py                # Abstract base models
│       ├── mixins.py
│       ├── utils.py
│       ├── validators.py
│       └── middleware.py
│
├── media/                           # User uploaded files
│   ├── portfolio/
│   ├── blog/
│   ├── testimonials/
│   └── uploads/
│
├── static/                          # Static files
│   ├── admin/
│   └── assets/
│
└── staticfiles/                     # Collected static files (production)

"""

# =============================================================================
# REQUIREMENTS.TXT
# =============================================================================

requirements_txt = """
# Core Django
Django==5.0.1
djangorestframework==3.14.0
django-cors-headers==4.3.1

# Database
psycopg2-binary==2.9.9  # PostgreSQL
# mysqlclient==2.2.0    # MySQL alternative

# Image Processing
Pillow==10.2.0
django-imagekit==5.0.0

# API Documentation
drf-spectacular==0.27.0

# Authentication & Security
djangorestframework-simplejwt==5.3.1
django-allauth==0.57.0

# Admin Enhancements
django-import-export==3.3.5
django-admin-interface==0.26.0

# Utilities
python-decouple==3.8
django-filter==23.5
django-extensions==3.2.3

# Storage (for production)
django-storages==1.14.2
boto3==1.34.14  # AWS S3  (Pending Install)

# Caching
django-redis==5.4.0
redis==5.0.1

# Development
django-debug-toolbar==4.2.0
ipython==8.20.0

# Testing (Pending install)
pytest==7.4.4
pytest-django==4.7.0
factory-boy==3.3.0
faker==22.0.0

# Production
gunicorn==21.2.0
whitenoise==6.6.0
"""

# =============================================================================
# .ENV TEMPLATE
# =============================================================================

env_template = """
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db
# Or for MySQL:
# DATABASE_URL=mysql://user:password@localhost:3306/portfolio_db

# CORS
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173

# AWS S3 (Optional - for production media storage)
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_STORAGE_BUCKET_NAME=
AWS_S3_REGION_NAME=us-east-1

# Email (Optional)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
EMAIL_USE_TLS=True

# Redis (Optional - for caching)
REDIS_URL=redis://localhost:6379/1

# JWT
JWT_SECRET_KEY=your-jwt-secret-key
"""

# =============================================================================
# BASE SETTINGS (config/settings/base.py)
# =============================================================================

base_settings = """
from pathlib import Path
from decouple import config
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'corsheaders',
    'django_filters',
    'drf_spectacular',
    'imagekit',
]

LOCAL_APPS = [
    'apps.portfolio',
    'apps.blog',
    'apps.services',
    'apps.resume',
    'apps.testimonials',
    'apps.site_config',
    'apps.common',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='portfolio_db'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

# CORS
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='').split(',')
CORS_ALLOW_CREDENTIALS = True

# API Documentation
SPECTACULAR_SETTINGS = {
    'TITLE': 'Portfolio API',
    'DESCRIPTION': 'API documentation for Portfolio Backend',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
}
"""

print("✅ Django Portfolio Backend Structure Generated!")
print("\nNext steps:")
print("1. Create virtual environment: python -m venv venv")
print("2. Activate it: source venv/bin/activate (Linux/Mac) or venv\\Scripts\\activate (Windows)")
print("3. Install requirements: pip install -r requirements.txt")
print("4. Create .env file with your configuration")
print("5. Run migrations: python manage.py migrate")
print("6. Create superuser: python manage.py createsuperuser")
print("7. Run server: python manage.py runserver")