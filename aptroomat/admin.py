# use geodjango admin instead of default
from django.contrib.gis import admin
from aptroomat.models import WorldBorder

# register world border administratoin site
admin.site.register(WorldBorder, admin.OSMGeoAdmin)
