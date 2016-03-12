from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin

from photos.urls import urlpatterns as photos_urls


urlpatterns = [
    url(r'^photos/', include(photos_urls, namespace='photos')),
    url(r'^admin/', admin.site.urls),
]


