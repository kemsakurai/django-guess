from rest_framework import generics

from .models import GuessResult
from .serializer import GuessResultSerializer
from .settings import GUESS_SETTINGS


class GuessResultList(generics.ListAPIView):
    serializer_class = GuessResultSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        page_path = self.kwargs.get('pagepath')
        effective_type = self.kwargs.get('effectivetype')
        print(effective_type)
        if not effective_type:
            effective_type = '3g'
        percent = GUESS_SETTINGS['PREFETCH_CONFIG'].get(effective_type);

        return GuessResult.objects.filter(previous_page_path=page_path, page_view_percent__gte=percent)
