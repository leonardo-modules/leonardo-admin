
from django.conf.urls import include, url
from leonardo.site import leonardo_admin
from ..urls import urlpatterns

urlpatterns += [
   url(r'^', include(leonardo_admin.urls)),
   url(r'^doc/', include('django.contrib.admindocs.urls')),
]