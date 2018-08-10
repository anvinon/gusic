from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.template.defaultfilters import urlencode


def index(request):
    form = SearchForm(request.GET or None)
    initialForm = InitialForm(request.GET or None)
    if initialForm.is_valid():
        initial = initialForm.cleaned_data["initial"]
        initial = int(initial)
        q = initialForm.choices[initial][1]
        artists = Artist.objects.filter(name__istartswith=q)
        artists_list = artists.values_list('name', flat=True)
        artists_list = list(artists_list)
        id = SearchHistory.objects.values_list('id', flat=True)
        word = SearchHistory.objects.values_list('word', flat=True)
        created_at = SearchHistory.objects.values_list('created_at', flat=True)
        history = zip(id, word, created_at)
        history = list(history)
        f = {
            'form': form,
            'initialForm': initialForm,
            'artists_list': artists_list,
            'history': history,
        }
        return render(request, 'search/index.html', f)
    else:
        f = {
            'form': form,
            'initialForm': initialForm,
        }
        return render(request, 'search/index.html', f)


def add(request):
    #    genre = GenreForm(request.GET or None)
    form = request.GET['name']
    sh = SearchHistory(word=form)
    sh.save()
    genres = []
    name = Artist.objects.filter(
        name__iexact=form).values_list('name', flat=True)[0]
    genre1 = Artist.objects.filter(
        name__iexact=form).values_list('genre1', flat=True)[0]
    genres.append(genre1)
    genre2 = Artist.objects.filter(
        name__iexact=form).values_list('genre2', flat=True)[0]
    genres.append(genre2)
    genre3 = Artist.objects.filter(
        name__iexact=form).values_list('genre3', flat=True)[0]
    genres.append(genre3)
    genre4 = Artist.objects.filter(
        name__iexact=form).values_list('genre4', flat=True)[0]
    genres.append(genre4)
    genre5 = Artist.objects.filter(
        name__iexact=form).values_list('genre5', flat=True)[0]
    genres.append(genre5)
    genre6 = Artist.objects.filter(
        name__iexact=form).values_list('genre6', flat=True)[0]
    genres.append(genre6)
    genre7 = Artist.objects.filter(
        name__iexact=form).values_list('genre7', flat=True)[0]
    genres.append(genre7)
    genre8 = Artist.objects.filter(
        name__iexact=form).values_list('genre8', flat=True)[0]
    genres.append(genre8)
    genre9 = Artist.objects.filter(
        name__iexact=form).values_list('genre9', flat=True)[0]
    genres.append(genre9)
    genres = list(filter(lambda a: a != '', genres))
    j = {
        'name': name,
        'genres': genres,
    }
    return render(request, 'search/add.html', j)


def other_artist(request):
    # ジャンル名をgetで取得
    genre = request.GET['name_list']
    # アーティスト名をgetで取得
    selected_artist = request.GET['name']
    selected_id = Artist.objects.filter(
        name__iexact=selected_artist).values_list('id', flat=True)[0]
    # ジャンルテーブルをジャンル名で検索
    genre_id = Genre.objects.filter(
        name__iexact=genre).values_list('id', flat=True)[0]
    # ジャンルとアーティストの外部テーブルを検索し、特定のジャンルに属する複数のアーティストのIDを取得
    artist_ids = ArtistAndGenre.objects.filter(
        genre_id=genre_id).values_list('artist_id', flat=True)
    artist_ids = list(artist_ids)
    artist_ids.remove(selected_id)
    artist_list = []
    for a in artist_ids:
        # songsテーブルを曲のIDで検索し、結果のタイトルを取得
        name = Artist.objects.filter(id=a).values_list('name', flat=True)[0]
        artist_list.append(name)
    f = {
        'selected_artist': selected_artist,
        'artist_list': artist_list
    }
    return render(request, 'search/other_artist.html', f)


def song(request):
    artist = request.GET['artist']
    songs = Songs.objects.filter(
        artist__iexact=artist, free_download=True).values_list('title', flat=True)
    songs = list(songs)
    f = {
        'songs': songs
    }
    return render(request, 'search/song.html', f)


def jump(request):
    song = request.GET['song']
    jump_url = Songs.objects.filter(
        title__iexact=song).values_list('url', flat=True)[0]
    return redirect('{0}'.format(jump_url))


def memo(request, search_id):
    print(search_id)
    return render(request, 'search/memo.html', {'search_id': search_id})
