from django.db import models
from django.utils import timezone

from .user import User


class DatasetTag(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    REQUIRED_FIELDS = [name]


class Dataset(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(DatasetTag)
    created_on = models.DateTimeField(default=timezone.now, db_index=True)
    figshare_id = models.IntegerField(primary_key=True)

    REQUIRED_FIELDS = [name, description, created_by, figshare_id]

    class Meta:
        ordering = ['-created_on']
