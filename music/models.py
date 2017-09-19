from django.db import models

class Album(models.model):
    artist = models.charfield(max_lenght=250)
    album_title = models.charfield(max_lenght=500)
    genre = models.charfield(max_lenght=100)
    album_logo = models.charfield(max_leght=1000)


class Songs(models.model):
    album = models.foreignkey(Album, on_delete=models.CASCADE)
    file_type = models.charfield(max_lenght=10)
    song_title = models.charfield(max_lenght=250)


