from supabase import create_client, Client
from pathlib import Path
import os
import socket
from decouple import config as _envConfig
from typing import Final

original_getaddrinfo = socket.getaddrinfo

def getaddrinfo_ipv4_first(host, port, family=0, type=0, proto=0, flags=0):
    # Try IPv4 first
    try:
        return original_getaddrinfo(host, port, socket.AF_INET, type, proto, flags)
    except socket.gaierror:
        # Fall back to default behavior
        return original_getaddrinfo(host, port, family, type, proto, flags)

socket.getaddrinfo = getaddrinfo_ipv4_first

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_a_$$!z+cs7#0#=rn9bd__x(ur!d6=t#+-&w98$%)!815uh4ro'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'backend', '*']

CORS_ALLOWED_ORIGINS = [
    "https://portfolio-3onx.onrender.com",
    "http://localhost:5173",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'rest_framework',
    "django_filters",

    'apps.blog.apps.BlogConfig',
    'apps.core.apps.CoreConfig',
    'apps.portfolio.apps.PortfolioConfig',
    'apps.resume.apps.ResumeConfig',
    'apps.services.apps.ServicesConfig',
    'apps.site_config.apps.SiteConfigConfig',
    'apps.testimonials.apps.TestimonialsConfig',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

ROOT_URLCONF = 'core_portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core_portfolio.wsgi.application'

# AUTH_USER_MODEL= 'app_portfolio.UserModel'

IS_PRODUCTION = _envConfig("IS_PRODUCTION", cast=bool)

SUPABASE_URL: Final[str] = _envConfig("SUPABASE_URL", cast=str)
SUPABASE_KEY: Final[str] = _envConfig("SUPABASE_KEY", cast=str)

assert SUPABASE_URL, "SUPABASE_URL is missing"
assert SUPABASE_KEY, "SUPABASE_KEY is missing"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
if IS_PRODUCTION:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': _envConfig('DB_NAME'),
            'USER': _envConfig('DB_USER'),
            'PASSWORD': _envConfig('DB_PASSWORD'),
            'HOST': _envConfig('DB_HOST'),  # Pooled URL
            'PORT': _envConfig('DB_PORT'),
            'DISABLE_SERVER_SIDE_CURSORS': _envConfig('SERVER_SIDE_CURSORS'),
            'OPTIONS': {
                'sslmode': 'require',
                'sslrootcert': os.path.join(BASE_DIR, 'supabase.crt'),
            },
            'CONN_MAX_AGE': 600,  # 10 minutes
            'CONN_HEALTH_CHECKS': _envConfig('DB_HEALTH_CHECK'),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
