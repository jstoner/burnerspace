from django.conf.urls.defaults import patterns, include, url

from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     (r'^media/(?P<path>.*)$', 'django.views.static.serve',
              {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
     (r'^accounts/', include('userena.urls')),
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     (r'^admin/', include(admin.site.urls)),
 )

