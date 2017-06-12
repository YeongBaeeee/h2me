# diary/models.py

from django.db import models
from django.conf import settings
from django.utils import timezone

class Diary(models.Model):
    STATUS_CHOICES = (
        ('s', 'Secret'),
        ('p', 'Public'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='diary_set')
    content = models.CharField(max_length=50, help_text='사진으로 대체')
    tags = models.CharField(max_length=50, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='위젯으로 대체')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

