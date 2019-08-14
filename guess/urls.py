from django.conf.urls import url
from .views import GuessResultList

urlpatterns = [
    url('^guessresult/(?P<pagepath>.+)/(?P<effectivetype>.+)/$', GuessResultList.as_view(), name='guess_result'),
    url('^guessresult/(?P<pagepath>.+)/$', GuessResultList.as_view(), name='guess_result_pagepath_only'),
]
