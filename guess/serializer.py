from rest_framework import serializers
from .models import GuessResult


class GuessResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuessResult
        fields = ('previous_page_path', 'page_path', 'page_view_percent', 'page_views')

