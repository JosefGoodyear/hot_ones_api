from rest_framework import serializers
from .models import Episode, HotSauce, Season

class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'

class HotSauceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotSauce
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'