from django.contrib.gis import forms, admin
from aptroomat.models import WorldBorder as world

class MultiPolygonAdmin(admin.GeoModelAdmin):
    list_filter = ('name', 'mpoly')
    list_display = ('name', 'mpoly', 'area', 'pop2005')

MPolyAdmin = MultiPolygonAdmin(world, admin.site)
MPolyGeom = world._meta.get_field('mpoly')
MPolyWidget = MPolyAdmin.get_map_widget(MPolyGeom)

class WorldBorderForm(forms.ModelForm):
    worldborder = forms.MultiPolygonField(
        widget = MPolyWidget(
            attrs = {
                'map_width': 1920,
                'map_height': 600,
            }
        )
    )

    class Meta:
        model = world

    class Media:
        js = ("http://openlayers.org/api/2.6/OpenLayers.js",)
