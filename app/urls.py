from django.urls import path
from app.views import MusicianListAndCreate, AlbumListAndCreate


urlpatterns = [
    path('musician/', MusicianListAndCreate.as_view()),
    path('album/', AlbumListAndCreate.as_view())
]

