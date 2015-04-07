from django.conf.urls import patterns, include, url
from aptroomat import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^explore/', views.explore, name='explore'),
    url(r'^api/', views.geojson, name='geojson'),
)
