from django.http import HttpResponse
from django.shortcuts import render
from django.template import RequestContext, loader


def index(request):
    enter = "start exploring"
    template = loader.get_template('aptroomat/index.html')
    context = RequestContext(request, {
        'enter': enter,
    })
    return HttpResponse(template.render(context))

def explore(request):
    enter = "can\'t stop exploring"
    template = loader.get_template('aptroomat/index.html')
    context = RequestContext(request, {
        'enter': enter,
    })
    return HttpResponse(template.render(context))
