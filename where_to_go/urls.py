from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from places.views import show_index, show_place

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_index),
    path('places/<int:id>/', show_place, name='place'),
    path('tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
