from django.conf.urls import patterns, url

urlpatterns = patterns('files.views',
                       url(r'^upload/$', 'upload', name='upload'),
                       url(r'^storage/(?P<token_key>\d+)$', 'storage', name='storage'),
)