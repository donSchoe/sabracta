from django.shortcuts import render
from aptroomat.models import WorldBorder
from aptroomat.forms import WorldBorderForm

def index(request):
    enter = "start exploring"
    context = { 'enter': enter }
    return render(request, 'aptroomat/index.html', context)

def explore(request):
    form = WorldBorderForm()
    layers = WorldBorder.objects.all()
    context = { 'form': form, 'layers': layers }
    return render(request, 'aptroomat/explore.html', context)
