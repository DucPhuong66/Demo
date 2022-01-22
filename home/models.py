from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Movie (models.Model):
    genre = models.CharField(_('genre'), max_length=225)
    artist_name = models.CharField(_('artist_name'), max_length=225)
    track_name = models.CharField(_('track_name'), max_length=225)
    track_id = models.IntegerField(_('track_id'))
    popularity = models.IntegerField(_('popularity'))
    acousticness = models.FloatField(_('acousticness'))
    danceability = models.FloatField(_('danceability'))
    duration_ms = models.BigIntegerField(_('duration_ms'))
    energy = models.FloatField(_('energy'))
    instrumentalness = models.FloatField(_('instrumentalness'))
    key = models.CharField(_('key'), max_length=150)
    liveness = models.FloatField(_('liveness'))
    loudness = models.FloatField(_('loudness'))
    mode = models.CharField(_('mode'), max_length=225)
    speechiness = models.FloatField(_('speechiness'))
    tempo = models.FloatField(_('tempo'))
    time_signature = models.DateField(_('time signature'), auto_now = True)
    valence = models.FloatField(_('valence'))


 





 
 


 

