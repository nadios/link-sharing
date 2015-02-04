from django.conf.urls import patterns, url

urlpatterns = patterns('files.views',
                       url(r'^upload/$', 'upload', name='upload'),
                       url(r'^files/(?P<token>\d+)$', 'storage', name='storage'),
)