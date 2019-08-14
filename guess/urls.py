from django.conf.urls import url
from .views import GuessResultList, CachedGuessResultList

urlpatterns = [
    url('^guessresult/(?P<pagepath>.+)/(?P<effectivetype>.+)/$', GuessResultList.as_view(), name='guess_result'),
    url('^guessresult/(?P<pagepath>.+)/$', GuessResultList.as_view(), name='guess_result_pagepath_only'),
    url('^cachedguessresult/(?P<pagepath>.+)/(?P<effectivetype>.+)/$', CachedGuessResultList.as_view(), name='cached_guess_result'),
    url('^cachedguessresult/(?P<pagepath>.+)/$', CachedGuessResultList.as_view(), name='cached_guess_result_pagepath_only'),
]
