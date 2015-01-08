from django.conf.urls import patterns, include, url
from .import views


urlpatterns = patterns('',
    url(r'^$', views.town_list),
    url(r'^town/(?P<pk>[0-9]+)/$', views.town_detail),
)
