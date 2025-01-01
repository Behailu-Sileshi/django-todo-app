from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from .validators import validate_deadline


class User(AbstractUser):
    email = models.EmailField(unique=True)


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title


class Task(models.Model):
    TASK_PENDING = "P"
    TASK_COMPLETED = "C"
    TASK_FAILED = "F"
    task_status = [
        (TASK_PENDING, "PENDING"),
        (TASK_COMPLETED, "COMPLETED"),
        (TASK_FAILED, "FAILED"),
    ]
    PRIORITY_HIGH = 'H'
    PRIORITY_MED = 'M'
    PRIORITY_LOW = 'L'
    
    task_priority = [
        (PRIORITY_HIGH, 'HIGH'),
        (PRIORITY_MED, 'MED'),
        (PRIORITY_LOW, 'LOW'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(
        null=True, blank=True, validators=[validate_deadline]
    )
    status = models.CharField(choices=task_status, default=TASK_PENDING, max_length=1)
    priority = models.CharField(choices=task_priority, default='M', max_length=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="tasks"
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(deadline__gt=models.F("created_at")),
                name="deadline_gt_creation_date",
            )
        ]
