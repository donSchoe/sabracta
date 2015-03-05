from django.conf.urls import patterns, include, url

# use geodjango admin instead of default
from django.contrib.gis import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
