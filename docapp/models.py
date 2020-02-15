from django.db import models
import datetime

class Commits(models.Model):
    Docid = models.CharField(max_length=50 , null=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50 , null=False)
    Document = models.CharField(max_length=10000 , null=False)
    sha = models.CharField(max_length=50 , null=False)
    isdiff = models.IntegerField(default=0, null=False)
    branch = models.CharField(max_length=50 , null=False, default='master')