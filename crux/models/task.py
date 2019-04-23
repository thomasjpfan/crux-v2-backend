from django.db import models
from django.utils import timezone

from .dataset import Dataset
from .dataset import User


class Task(models.Model):
    name = models.CharField(max_length=300)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=timezone.now)

    REQUIRED_FIELDS = [name, dataset, created_by]
