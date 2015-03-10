# using floppyforms 1.3.0
import floppyforms as forms
from aptroomat.models import WorldBorder

class MultiPolygonWidget(forms.gis.MultiPolygonWidget, forms.gis.BaseOsmWidget):
    pass

class WorldPolygonWidget(MultiPolygonWidget):
    map_width = 1024
    map_height = 600

class WorldBorderForm(forms.Form):

#    class Meta:
#        model = WorldBorder
#        widgets = {
#           'geom': WorldPolygonWidget,
#        }

    world = forms.gis.MultiPolygonField(widget=WorldPolygonWidget)
