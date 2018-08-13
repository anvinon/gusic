import django
django.setup()
from .models import Artist
from .models import Songs
from .models import ArtistAndSongs


def insert_songs():
    for r in range(4065, 7828):
        # songsテーブルのidでの検索結果
        song_query = Songs.objects.filter(id=r)
        # アーティスト名が入っている
        a = song_query.values_list('artist', flat=True)[0]
        # 余分な先頭と末尾の半角スペースを削除しておく
        a = a.strip()
        # artistテーブルのアーティスト名での検索結果
        artist_query = Artist.objects.filter(name=a)
        # artistテーブルのid
        a_id = artist_query.values_list('id', flat=True)[0]
        # artistandsongsテーブルに、songsテーブルのidとartistテーブルのidを紐付けて保存
        aas = ArtistAndSongs(artist_id=a_id, song_id=r)
        aas.save()


insert_songs()
