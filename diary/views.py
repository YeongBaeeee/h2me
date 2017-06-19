# diary/views.py

"""

    views.py
    ~~~~~~~~

"""

from django.shortcuts import render
from .models import Diary, Comment, Tag
from el_pagination.decorators import page_template


@page_template('diary/diary_list_page.html')  # just add this decorator
def diary_list(request,
        template='diary/index.html', extra_context=None):
    context = {
        'diary_list': Diary.objects.all(),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render(request, template, context)
