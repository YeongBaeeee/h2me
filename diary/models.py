# diary/models.py

from django.db import models
from django.utils import timezone

class Diary(models.Model):
    content = models.CharField(max_length=50, help_text='사진으로 대체')
    tags = models.CharField(max_length=50, blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='위젯으로 대체')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

