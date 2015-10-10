
from django.conf.urls import include, patterns, url

from leonardo.site import leonardo_admin
from constance import config


urlpatterns = patterns('',
                       url(r'^%sdoc/' % config.ADMIN_URL, include('django.contrib.admindocs.urls')),
                       url(r'^%s' % config.ADMIN_URL, include(leonardo_admin.urls)),
                       )
