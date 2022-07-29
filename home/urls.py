from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.staticfiles.views import serve

from django.conf.urls.static import static


urlpatterns = [
    path('trkadmin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('index.urls')),
    path('news/', include('newsapp.urls')),
]

# handler404 = "index.views.page_not_found_view"


if settings.DEBUG:
    urlpatterns += [
      path(r'^media/(?P<path>.*)$', serve),
      path(r'^static/(?P<path>.*)$', serve),
    ]

admin.site.site_header = 'Администрирование ТРК'