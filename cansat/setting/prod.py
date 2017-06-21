import os
from .common import *

import pymysql
pymysql.install_as_MySQLdb()

DEBUG = True

INSTALLED_APPS += ['storages']

DATABASES = {
    'default': {
            'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
            'HOST': os.environ.get('DB_HOST', 'ja-cdbr-azure-east-a.cloudapp.net'),
            'NAME': os.environ.get('DB_NAME', 'cansat_triplee'),
            'USER': os.environ.get('DB_USER', ''),
            'PASSWORD': os.environ.get('DB_PASSWORD', ''),
            'PORT': os.environ.get('DB_PORT', 3306),
        },
}
STATICFILES_STORAGE = 'mysite.storages.StaticAzureStorage' # FIXME: 프로젝트 내, storages 지정
DEFAULT_FILE_STORAGE = 'mysite.storages.MediaAzureStorage' # FIXME: 프로젝트 내, storages 지정
# 설정 / 액세스 키
AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME', 'cansat')
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY', 'yGx1Ijpo1EAPpgLknwo8uDuEqP9vjVBoosYFfRObnPuqgbKAd5dUxT3/9M7FwAhv42t3D14spt5gHy5JeUKRmw==')
AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER', 'static') # static 파일 저장/서빙용 컨테이너
AZURE_MEDIA_CONTAINER = os.environ.get('AZURE_MEDIA_CONTAINER', 'media') # media 파일 저장/서빙용 커스텀 컨테이너
