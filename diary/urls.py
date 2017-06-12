# diary/urls.py

from django.conf.urls import url
from. import views

urlpatterns = [
    url(r'^$', views.diary_list,  name='diary_list'),
]