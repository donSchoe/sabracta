from django.conf.urls import patterns, include, url
from aptroomat import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
