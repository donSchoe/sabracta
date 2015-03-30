from django.shortcuts import render
from aptroomat.forms import WorldBorderForm as form

def index(request):
    enter = "start exploring"
    context = { 'enter': enter }
    return render(request, 'aptroomat/index.html', context)

def explore(request):
    context = { 'form': form }
    return render(request, 'aptroomat/explore.html', context)
