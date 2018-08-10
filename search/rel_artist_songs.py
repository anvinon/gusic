import django
django.setup()
from .models import *


def rel_artist_songs():
    for r in range(10215, 12731):
        try:
            # artistテーブルのidがrでの検索結果
            artist_query = Artist.objects.filter(id=r)
            # idがrの場合のnameカラムの値が入っている
            name = artist_query.values_list('name', flat=True)[0]
            # songsテーブルのジャンル名での検索結果
            songs_query = Songs.objects.filter(artist=name)
            # songsテーブルのidが入っている
            song_ids = songs_query.values_list('id', flat=True)
            for s in song_ids:
                # artistandsongsテーブルに、songsテーブルのidとartistテーブルのidを紐付けて保存
                aag = ArtistAndSongs(song_id=s, artist_id=r)
                aag.save()
        except:
            print("artistテーブルのID")
            print(r)
            print("でエラー発生")
rel_artist_songs()
