from rest_framework import generics

from .models import GuessResult
from .serializer import GuessResultSerializer
from .settings import GUESS_SETTINGS
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class GuessResultList(generics.ListAPIView):
    serializer_class = GuessResultSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        page_path = self.kwargs.get('pagepath')
        if not page_path:
            return Response("page_path is required.", status=status.HTTP_400_BAD_REQUEST)

        effective_type = self.kwargs.get('effectivetype')
        if not effective_type:
            effective_type = '3g'
        percent = GUESS_SETTINGS['PREFETCH_CONFIG'].get(effective_type);

        return GuessResult.objects.filter(previous_page_path=page_path, page_view_percent__gte=percent)


class CachedGuessResultList(GuessResultList):
    @method_decorator(cache_page(60 * 60 * 4))
    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response
