from django.conf.urls import url
from .views import GuessResultList, CachedGuessResultList

urlpatterns = [
    url(r'^guessresult/(?P<pagepath>.+)/(?P<effectivetype>.+)/$', GuessResultList.as_view(), name='guess_result'),
    url(r'^guessresult/(?P<pagepath>.+)/$', GuessResultList.as_view(), name='guess_result_pagepath_only'),
    url(r'^cachedguessresult/(?P<pagepath>.+)/(?P<effectivetype>.+)/$', CachedGuessResultList.as_view(), name='cached_guess_result'),
    url(r'^cachedguessresult/(?P<pagepath>.+)/$', CachedGuessResultList.as_view(), name='cached_guess_result_pagepath_only'),
]
