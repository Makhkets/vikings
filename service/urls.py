"""vikings URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import  service.views


urlpatterns = [
    path("", service.views.index, name="upload_photo_page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
