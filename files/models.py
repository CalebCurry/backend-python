from django.db import models

class File(models.Model):
    name = models.CharField(max_length=1024)
    upload_timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
    def __str__(self):
        return self.name