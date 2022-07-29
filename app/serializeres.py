from rest_framework import serializers
from app.models import Musician, Album


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ['id', 'name', 'last_name', 'instrument']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'id', 'artist', 'name', 'released', 'stars']
