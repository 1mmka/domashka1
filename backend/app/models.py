from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    status = models.BooleanField(default=False)