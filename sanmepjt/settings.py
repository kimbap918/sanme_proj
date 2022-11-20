"""
Django settings for sanmepjt project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
import os, json
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

load_dotenv()

# SECRET_KEY 파일 위치
secret_file = os.path.join(BASE_DIR, "secrets.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())

# secrets.json 파일에서 SECRET_KEY 가져오기
def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")
# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = [
    "Sanmebeanstalk-env.eba-4rfc539i.ap-northeast-2.elasticbeanstalk.com",
    "127.0.0.1",
    "localhost",
]


# Application definition

INSTALLED_APPS = [
    # aws setting
    "storages",
    # chat
    "channels",
    "chat",
    # apps
    "accounts",
    "articles",
    # module
    "maps",
    "django_bootstrap5",
    "django_extensions",
    "django_cleanup.apps.CleanupConfig",
    "imagekit",
    "corsheaders",
    "widget_tweaks",
    "multiselectfield",
    "embed_video",
    # django default
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
ASGI_APPLICATION = "sanmepjt.asgi.application"


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sanmepjt.urls"

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

WSGI_APPLICATION = "sanmepjt.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# 기존 기본값
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STC_ROOT = "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]


# Media files
# MEDIA_ROOT = BASE_DIR / "media"
# MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

# 미디어 개발과 배포환경 분리
DEBUG = os.getenv("DEBUG") == "True"

if DEBUG:
    MEDIA_ROOT = BASE_DIR / "media"
    MEDIA_URL = "/media/"

else:
    # DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
    DEFAULT_FILE_STORAGE = "sanmepjt.storages.MediaStorage"

    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
    AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")

    AWS_REGION = "ap-northeast-2"
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (
        AWS_STORAGE_BUCKET_NAME,
        AWS_REGION,
    )

# 데이터베이스 개발과 배포환경 분리
if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("sanme_rds"),  # db이름
            "USER": "postgres",
            "PASSWORD": os.getenv("sanme1313"),  # RDS 마스터암호
            "HOST": os.getenv(
                "sanme.cvprnt3cn8kv.ap-northeast-2.rds.amazonaws.com"
            ),  # 엔드포인트
            "PORT": "5432",  # 포트
        }
    }


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "accounts.User"

ASGI_APPLICATION = "sanmepjt.routing.application"

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("127.0.0.1", 6379)],
        },
    },
}
