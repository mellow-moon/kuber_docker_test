from django.db import models


class TaskModel(models.Model):
    task_name = models.CharField(max_length=100)
    task_id = models.CharField(unique=True, max_length=100)
    is_revoked = models.BooleanField(default=False)
