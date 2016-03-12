from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from photos.urls import urlpatterns as photos_urls


urlpatterns = [
    url(r'^photos/', include(photos_urls, namespace='photos')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

