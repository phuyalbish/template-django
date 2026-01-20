import os
from pathlib import Path

import environ
import cloudinary
import cloudinary.api
import cloudinary.uploader

from core.config import REFRESH_LIFETIME, TOKEN_LIFETIME

# --------------------------------------------------
# Base directory
# --------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------------------------------------
# Environment variables
# --------------------------------------------------
env = environ.Env(
    DEBUG=(bool, False),
    DEFAULT_DB=(str, "sqlite"),
)

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

# Extra Variables

DEFAULT_SUPERUSER_USERNAME = env("DEFAULT_SUPERUSER_USERNAME")
DEFAULT_SUPERUSER_PASSWORD = env("DEFAULT_SUPERUSER_PASSWORD")

# --------------------------------------------------
# Core settings
# --------------------------------------------------
DEBUG = env.bool("DEBUG")
SECRET_KEY = env("SECRET_KEY")


# --------------------------------------------------
# Environment-based security
# --------------------------------------------------


if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CORS_ALLOW_ALL_ORIGINS = True

    # Ensure no HTTPS redirects in development
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
else:
    ALLOWED_HOSTS = [
        host.strip()
        for host in env("ALLOWED_HOSTS").split(",")
        if host.strip()
    ]

    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = [
        cors.strip()
        for cors in env("CORS_ALLOWED_ORIGINS").split(",")
        if cors.strip()
    ]

    # Extra Security
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS



# --------------------------------------------------
# Installed apps
# --------------------------------------------------
INSTALLED_APPS = [
    "jazzmin",
    "colorfield",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "tinymce",
    "cloudinary",
    "django_extensions",
    "users",
    "contacts",
    "dummys",
]

# --------------------------------------------------
# Middleware
# --------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"
WSGI_APPLICATION = "core.wsgi.application"

# --------------------------------------------------
# Templates
# --------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# --------------------------------------------------
# Database
# --------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
        "OPTIONS": {"autocommit": True},
    },
    # "sqlite": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # },
    # "postgresql": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": env("DB_NAME"),
    #     "USER": env("DB_USER"),
    #     "PASSWORD": env("DB_PASSWORD"),
    #     "HOST": env("DB_HOST"),
    #     "PORT": env("DB_PORT"),
    # },
}

# --------------------------------------------------
# Auth
# --------------------------------------------------
AUTH_USER_MODEL = "users.Users"

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]



# --------------------------------------------------
# Email
# --------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

# --------------------------------------------------
# Localization
# --------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------
# Static & media
# --------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = "staticfiles/"
STATICFILES_DIRS = [BASE_DIR / "static"]



STATIC_URL = "static/"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --------------------------------------------------
# DRF & JWT
# --------------------------------------------------
REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": TOKEN_LIFETIME,
    "REFRESH_TOKEN_LIFETIME": REFRESH_LIFETIME,
    "AUTH_HEADER_TYPES": ("Bearer",),
}

# --------------------------------------------------
# Cloudinary
# --------------------------------------------------
cloudinary.config(
    cloud_name=env("CLOUDINARY_CLOUD_NAME"),
    api_key=env("CLOUDINARY_API_NAME"),
    api_secret=env("CLOUDINARY_API_SECRET"),
)

# --------------------------------------------------
# Logging
# --------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "django_errors.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}


JAZZMIN_SETTINGS = {
    "site_title": "PROJECT_NAME",
    "site_header": "PROJECT_NAME",
    "site_brand": "PROJECT_NAME",
    "welcome_sign": "Welcome to PROJECT_NAME Admin Panel",

    "custom_css": "css/custom_admin.css",
    "custom_js": "js/custom_admin.js",
    
    "brand_logo_xl": "images/image.webp",
    "brand_logo": "images/image.webp",

    "site_logo": "images/image.webp",
    "site_icon": "images/image.webp",

    "collapse_apps": True,
    "related_modal_active": True,
    "order_with_respect_to": ["dummys", "contacts", "users", "groups"],


    "collapse_apps_initially": [
        "users", "dummys", "contacts",
    ],


    "icons": {
        "auth": "fas fa-users-cog",
        "users.Users": "fas fa-user",
        "auth.Group": "fas fa-user-shield",

        "contacts.Contact": "fas fa-address-book",

        "dummys.Dummy": "fas fa-hands-helping",

     
    },


    "theme": {
        "sidebar": {
            "background": "#0000ff",
            "text": "#ecf0f1",
            "brand_background": "#1abc9c",
            "brand_text": "#ffffff",
            "nav_item_hover_background": "#16a085",
            "nav_item_hover_text": "#ffffff",
            "nav_item_active_background": "#2980b9",
            "nav_item_active_text": "#ffffff",
        },
    },
}
