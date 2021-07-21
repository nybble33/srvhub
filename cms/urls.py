# -*- coding: utf-8 -*-

from django.conf.urls import url

from cms.views import index, variant_1

urlpatterns = [
    url(r'^$', index),
    url(r'^var-1/$', variant_1)
]
