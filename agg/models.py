from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    site = models.CharField(max_length=5)
    link = models.CharField(max_length=300)
    
    published = models.DateTimeField(null=True, default=None)
    date_added = models.DateTimeField(auto_now_add=True)

    applied = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)
