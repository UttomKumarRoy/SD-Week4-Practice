from django.shortcuts import render, get_object_or_404, redirect
from .models import Musician, Album
from .forms import MusicianForm, AlbumForm

def index(request):
    return render(request, 'musicians/index.html')

def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, 'musicians/musician_list.html', {'musicians': musicians})


def musician_detail(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    albums = Album.objects.filter(musician=musician)
    return render(request, 'musicians/musician_detail.html', {'musician': musician, 'albums': albums})

def edit_musician(request, musician_id):
    musician = get_object_or_404(Musician, id=musician_id)
    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musician_detail', musician_id=musician.id)
    else:
        form = MusicianForm(instance=musician)
    return render(request, 'musicians/edit_musician.html', {'form': form, 'musician': musician})

def edit_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('musician_detail', musician_id=album.musician.id)
    else:
        form = AlbumForm(instance=album)
    return render(request, 'musicians/edit_album.html', {'form': form, 'album': album})

def delete_album(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    musician_id = album.musician.id
    album.delete()
    return redirect('musician_detail', musician_id=musician_id)
