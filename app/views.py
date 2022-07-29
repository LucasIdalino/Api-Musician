from rest_framework import generics
from app.models import Musician, Album
from app.serializeres import MusicianSerializer, AlbumSerializer


class MusicianListAndCreate(generics.ListCreateAPIView):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer


class AlbumListAndCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
