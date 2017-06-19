# diary/models.py

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils import timezone

class Diary(models.Model):
    STATUS_CHOICES = (
        ('s', 'Secret'),
        ('p', 'Public'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='diary_set')
    content = models.CharField(max_length=50, help_text='사진으로 대체')
    tag_set = models.ManyToManyField('Tag', blank=True)
    lnglat = models.CharField(max_length=50, blank=True, help_text='위젯으로 대체')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('diary:diary_list', args=[self.id])


class Comment(models.Model):
    diary = models.ForeignKey(Diary)
    author = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True) #같은 테그테이블에 테그이름이 겹치지 않게..

    def __str__(self):
        return self.name