# photos/urls.py
from django.conf.urls import url

from . import views


app_name = 'photos'

urlpatterns = [
    url(r'^$', views.toppage, name='toppage'),
]

