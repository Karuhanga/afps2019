from presence.aws.conf import *

from .base import *

import dj_database_url

#PROD##############################################
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES = {
    'default': db_from_env
}
DEBUG = True
###################################################
