from django.contrib import admin
from .models import Musician, Album

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'instrument_type')

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'album_name', 'musician', 'release_date', 'rating')
