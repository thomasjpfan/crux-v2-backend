from django.db import models
from django.utils import timezone

from .dataset import Dataset
from .dataset import User
from .task import Task


class AnalysisTag(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    REQUIRED_FIELDS = [name]


class Analysis(models.Model):
    name = models.CharField(max_length=300, db_index=True)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(AnalysisTag)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, null=True, on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(default=timezone.now, db_index=True)
    figshare_id = models.IntegerField()

    REQUIRED_FIELDS = [name, created_by, dataset, figshare_id]

    class Meta:
        verbose_name_plural = 'Analyses'
        ordering = ['-created_on']
