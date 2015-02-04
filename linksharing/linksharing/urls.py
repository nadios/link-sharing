from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('files.views',
                       url(r'^upload/$', 'upload', name='upload'),
                       url(r'^storage/(?P<token_key>.*)$', 'storage', name='storage'),
                       url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)