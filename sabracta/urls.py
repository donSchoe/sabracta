from django.conf.urls import patterns, include, url

# use geodjango admin instead of default
from django.contrib.gis import admin
import aptroomat

urlpatterns = patterns('',
    url(r'^aptroomat/', include('aptroomat.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
