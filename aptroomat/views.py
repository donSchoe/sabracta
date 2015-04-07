from django.shortcuts import render
from aptroomat.forms import WorldBorderForm
from aptroomat.models import WorldBorder

def index(request):
    enter = "start exploring"
    context = { 'enter': enter }
    return render(request, 'aptroomat/index.html', context)

def explore(request):
    form = WorldBorderForm()
    context = { 'form': form }
    return render(request, 'aptroomat/explore.html', context)

def geojson(request):
    layers = WorldBorder.objects.all()
    context = { 'layers': layers }
    return render(request, 'aptroomat/geojson.json', context)
