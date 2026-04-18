# backend/config/settings.py

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "django-secret-key"
DEBUG = True

ALLOWED_HOSTS = []

# ========================
# INSTALLED APPS
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',

    # Custom Apps
    'apps.books',
    'apps.rag',
]

# ========================
# MIDDLEWARE (FIXED)
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',   # ✅ REQUIRED
    'django.contrib.messages.middleware.MessageMiddleware',       # ✅ REQUIRED
]

# ========================
# ROOT URL
# ========================
ROOT_URLCONF = 'config.urls'

# ========================
# TEMPLATES (VERY IMPORTANT FIX)
# ========================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# ========================
# DATABASE
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========================
# STATIC
# ========================
STATIC_URL = 'static/'

# ========================
# DEFAULT PRIMARY KEY FIX
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ========================
# REDIS (optional)
# ========================
REDIS_HOST = "localhost"
REDIS_PORT = 6379

# ========================
# DRF CONFIG
# ========================
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ]
}

# ========================
# CHROMA DB
# ========================
CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")