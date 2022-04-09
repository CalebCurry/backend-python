from django.db import models

class File(models.Model):
    name = models.CharField(max_length=1024)
    file_type = models.CharField(max_length=1024)
    upload_timestamp = models.IntegerField(default=0)