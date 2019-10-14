from django.db import models


class Season(models.Model):
    season_id = models.IntegerField(primary_key=True)
    number_of_episodes = models.IntegerField()

    def __str__(self):
        return str(self.season_id)

class Episode(models.Model):
    episode_id = models.IntegerField(primary_key=True)
    guest = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    episode_in_season = models.IntegerField()
    title = models.TextField(default='')
    link = models.URLField(default='')
    completed = models.BooleanField(default=True)
    dab = models.BooleanField(default=True)
    vegan = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.episode_id)

class HotSauce(models.Model):
    hotsauce_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    scoville_units = models.IntegerField()
    seasons = models.ManyToManyField(Season)

    def __str__(self):
        return self.name
