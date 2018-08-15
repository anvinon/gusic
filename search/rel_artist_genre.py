import django
django.setup()
from .models import Artist, Genre, ArtistAndGenre


def rel_artist_genre():
    for r in range(10215, 12731):
        # artistテーブルのidがrでの検索結果
        artist_query = Artist.objects.filter(id=r)
        # genre1カラムのidがrの場合の値が入っている
        genre1 = artist_query.values_list('genre1', flat=True)[0]
        # 余分な先頭と末尾の半角スペースを削除しておく
        genre1 = genre1.strip()
        # genreテーブルのジャンル名での検索結果
        genre1_query = Genre.objects.filter(name=genre1)
        # artistテーブルのidが入っている
        genre1_id = genre1_query.values_list('id', flat=True)[0]
        if genre1_id == 1694:
            pass
        else:
            # artistandgenreテーブルに、genreテーブルのidとartistテーブルのidを紐付けて保存
            aag = ArtistAndGenre(genre_id=genre1_id, artist_id=r)
            aag.save()

        artist_query = Artist.objects.filter(id=r)
        genre2 = artist_query.values_list('genre2', flat=True)[0]
        genre2 = genre2.strip()
        genre2_query = Genre.objects.filter(name=genre2)
        genre2_id = genre2_query.values_list('id', flat=True)[0]
        if genre2_id == 1694:
            pass
        else:
            aag = ArtistAndGenre(genre_id=genre2_id, artist_id=r)
            aag.save()

        artist_query = Artist.objects.filter(id=r)
        genre3 = artist_query.values_list('genre3', flat=True)[0]
        genre3 = genre3.strip()
        genre3_query = Genre.objects.filter(name=genre3)
        genre3_id = genre3_query.values_list('id', flat=True)[0]
        if genre3_id == 1694:
            pass
        else:
            # artistandgenreテーブルに、genreテーブルのidとartistテーブルのidを紐付けて保存
            aag = ArtistAndGenre(genre_id=genre3_id, artist_id=r)
            aag.save()

        artist_query = Artist.objects.filter(id=r)
        genre4 = artist_query.values_list('genre4', flat=True)[0]
        genre4 = genre4.strip()
        genre4_query = Genre.objects.filter(name=genre4)
        genre4_id = genre4_query.values_list('id', flat=True)[0]
        if genre4_id == 1694:
            pass
        else:
            # artistandgenreテーブルに、genreテーブルのidとartistテーブルのidを紐付けて保存
            aag = ArtistAndGenre(genre_id=genre4_id, artist_id=r)
            aag.save()

        artist_query = Artist.objects.filter(id=r)
        genre5 = artist_query.values_list('genre5', flat=True)[0]
        genre5 = genre5.strip()
        genre5_query = Genre.objects.filter(name=genre5)
        genre5_id = genre5_query.values_list('id', flat=True)[0]
        if genre5_id == 1694:
            pass
        else:
            aag = ArtistAndGenre(genre_id=genre5_id, artist_id=r)
            aag.save()

        artist_query = Artist.objects.filter(id=r)
        genre6 = artist_query.values_list('genre6', flat=True)[0]
        genre6 = genre6.strip()
        genre6_query = Genre.objects.filter(name=genre6)
        genre6_id = genre6_query.values_list('id', flat=True)[0]
        if genre6_id == 1694:
            pass
        else:
            aag = ArtistAndGenre(genre_id=genre6_id, artist_id=r)
            aag.save()

        artist_query = Artist.objects.filter(id=r)
        genre7 = artist_query.values_list('genre7', flat=True)[0]
        genre7 = genre7.strip()
        genre7_query = Genre.objects.filter(name=genre7)
        genre7_id = genre7_query.values_list('id', flat=True)[0]
        if genre7_id == 1694:
            pass
        else:
            aag = ArtistAndGenre(genre_id=genre7_id, artist_id=r)
            aag.save()

        artist_query = Artist.objects.filter(id=r)
        genre8 = artist_query.values_list('genre8', flat=True)[0]
        genre8 = genre8.strip()
        genre8_query = Genre.objects.filter(name=genre8)
        genre8_id = genre8_query.values_list('id', flat=True)[0]
        if genre8_id == 1694:
            pass
        else:
            aag = ArtistAndGenre(genre_id=genre8_id, artist_id=r)
            aag.save()

        artist_query = Artist.objects.filter(id=r)
        genre9 = artist_query.values_list('genre9', flat=True)[0]
        genre9 = genre9.strip()
        genre9_query = Genre.objects.filter(name=genre9)
        genre9_id = genre9_query.values_list('id', flat=True)[0]
        if genre9_id == 1694:
            pass
        else:
            aag = ArtistAndGenre(genre_id=genre9_id, artist_id=r)
            aag.save()


rel_artist_genre()
