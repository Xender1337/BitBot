__author__ = 'Xender'
from django.conf.urls import patterns, url
from Trade import views

urlpatterns = patterns('',
                       url(r'^$',              view=views.index,   name='index'))
