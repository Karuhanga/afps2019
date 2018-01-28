import datetime

AWS_ACCESS_KEY_ID = "AKIAJHX7IAPZXAVZGCMQ"
AWS_SECRET_ACCESS_KEY = "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"
AWS_FILE_EXPIRE = 200
AWS_PRELOAD_METADATA = True
AWS_S3_FILE_OVERWRITE = False
AWS_QUERYSTRING_AUTH = False

MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'presence.aws.utils.MediaRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'afps2019'
S3DIRECT_REGION = 'us-east-1'
S3_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = '//%s.s3.amazonaws.com/media/' % AWS_STORAGE_BUCKET_NAME
MEDIA_ROOT = MEDIA_URL

two_months = datetime.timedelta(days=61)
date_two_months_later = datetime.date.today() + two_months
expires = date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_S3_OBJECT_PARAMETERS = {
    'Expires': expires,
    'CacheControl': 'max-age=%d' % (int(two_months.total_seconds()), ),
}
