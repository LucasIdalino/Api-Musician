from django.db import models


class Musician(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=50)


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    released = models.DateField()
    stars = models.IntegerField()
