# use postgis model instead of default
from django.contrib.gis.db import models

# world borders database model based on data/TM_WORLD_BORDERS-0.3.shp layout
class WorldBorder(models.Model):

    # regular django postgresql database fields
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # geodjango specific fields for the postgis backend
    mpoly = models.MultiPolygonField()

    # overriding the default manager with a geomanager
    objects = models.GeoManager()

    # returns the string representation of the model
    def __str__(self):
        return self.name
