from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from custom_functions.check_connection import check_connection

urlpatterns = [
    path('admin/', admin.site.urls),
    path("events/", include('events.urls')),
    path("users/", include('users.urls')),
    path('checkConnection/', check_connection),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "C-Techs Data Management Console"
admin.site.site_title = 'Things to You'

