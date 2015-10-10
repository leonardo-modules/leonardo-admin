
from django.conf.urls import include, url

from leonardo.site import leonardo_admin
from constance import config


urlpatterns = [
   url(r'^%sdoc/' % config.ADMIN_URL, include('django.contrib.admindocs.urls')),
   url(r'^%s' % config.ADMIN_URL, include(leonardo_admin.urls)),
]
