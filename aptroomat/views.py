from django.shortcuts import render
import floppyforms as forms
from aptroomat.forms import WorldBorderForm

def index(request):
    enter = "start exploring"
    context = { 'enter': enter }
    return render(request, 'aptroomat/index.html', context)

def explore(request):
    form = WorldBorderForm()
    context = { 'form': form }
    return render(request, 'aptroomat/explore.html', context)
