from django.db import models
from django.template.defaultfilters import default


class Artist(models.Model):
    name = models.CharField(max_length=255)
    genre1 = models.CharField(max_length=255, blank=True, null=True)
    genre2 = models.CharField(max_length=255, blank=True, null=True)
    genre3 = models.CharField(max_length=255, blank=True, null=True)
    genre4 = models.CharField(max_length=255, blank=True, null=True)
    genre5 = models.CharField(max_length=255, blank=True, null=True)
    genre6 = models.CharField(max_length=255, blank=True, null=True)
    genre7 = models.CharField(max_length=255, blank=True, null=True)
    genre8 = models.CharField(max_length=255, blank=True, null=True)
    genre9 = models.CharField(max_length=255, blank=True, null=True)

class Genre(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Songs(models.Model):
    id = models.IntegerField
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    free_download = models.BooleanField(default=False)
    url = models.URLField(blank = True)
    
class ArtistAndSongs(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song = models.ForeignKey(Songs, on_delete=models.CASCADE)

class ArtistAndGenre(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class SearchHistory(models.Model):
    word = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
