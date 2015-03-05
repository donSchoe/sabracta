from django.shortcuts import render

def index(request):
    enter = "start exploring"
    context = { 'enter': enter }
    return render(request, 'aptroomat/index.html', context)

def explore(request):
    enter = "can\'t stop exploring"
    context = { 'enter': enter }
    return render(request, 'aptroomat/index.html', context)
