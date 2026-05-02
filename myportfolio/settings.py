from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',  # your app
]
IS_PRODUCTION = os.environ.get('RENDER') == 'true'
DEBUG = not IS_PRODUCTION
ALLOWED_HOSTS = []
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'main' / 'templates'],  # or just [] if not using custom paths
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
STATIC_URL = 'static/'
ROOT_URLCONF = 'myportfolio.urls'
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-$3cr3t-k3y-for-dev-1234567890')
STATICFILES_DIRS = [BASE_DIR / "main" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,127.0.0.2,localhost').split(',')

# Security settings for HTTPS (Render serves over HTTPS)
SECURE_SSL_REDIRECT = IS_PRODUCTION
SECURE_HSTS_SECONDS = 31536000 if IS_PRODUCTION else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = IS_PRODUCTION
SECURE_HSTS_PRELOAD = IS_PRODUCTION
SESSION_COOKIE_SECURE = IS_PRODUCTION
CSRF_COOKIE_SECURE = IS_PRODUCTION

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
