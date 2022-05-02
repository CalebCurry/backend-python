from storages.backends.s3boto3 import S3Boto3Storage
class PrivateMediaStorage(S3Boto3Storage):
    custom_domain = False