__author__ = 'Sanket'
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^/', include(contact.urls)),
)
