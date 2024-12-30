from django.db import models
from django.conf import settings

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Task(models.Model):
    TASK_PENDING = 'P'
    TASK_COMPLETED = 'C'
    TASK_FAILED = 'F'
    task_status = [
        (TASK_PENDING, 'PENDING' ),
        (TASK_COMPLETED, 'COMPLETED'),
        (TASK_FAILED, 'FAILED')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(choices=task_status, default=TASK_PENDING, max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')