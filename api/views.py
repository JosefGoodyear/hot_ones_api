from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import EpisodeSerializer, HotSauceSerializer, SeasonSerializer
from .models import Episode, HotSauce, Season

class EpisodeView(viewsets.ReadOnlyModelViewSet):
    """
    Returns all regular episodes of Hot Ones
    Search is enabled by name of guest(s).
    """
    queryset = Episode.objects.all().order_by('episode_id')
    serializer_class = EpisodeSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['guest']

class HotSauceView(viewsets.ReadOnlyModelViewSet):
    """
    Returns all hot sauces used on Hot Ones.
    Search is enabled by name of hot sauce.
    """
    queryset = HotSauce.objects.all().order_by('hotsauce_id')
    serializer_class = HotSauceSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ['name']


class SeasonView(viewsets.ReadOnlyModelViewSet):
    """
    Returns a list of all seasons of Hot Ones

    """
    queryset = Season.objects.all().order_by('season_id')
    serializer_class = SeasonSerializer