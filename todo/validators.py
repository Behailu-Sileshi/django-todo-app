from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_deadline(value):
    if value < timezone.now():
        raise ValidationError("Date time can not be in the past.")
