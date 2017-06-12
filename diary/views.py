# diary/views.py

from django.shortcuts import render


def diary_list(request):
    return render(request, 'diary/index.html')
