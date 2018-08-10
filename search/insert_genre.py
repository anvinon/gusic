import django
django.setup()
from .models import Genre, Artist

def insert_genre() :
    for a in range(10215, 12731) :
        # artistテーブルからidでの検索結果を代入
        artist = Artist.objects.filter(id = a)
        try :
            # 検索結果のうち、genre1カラムの値を代入
            genre1 = artist.values_list('genre1', flat = True)[0]
            genre1 = genre1.strip()
            # genre1の値が既にgenreテーブルに存在したら何もしない
            # そうでなければ、保存
            if Genre.objects.filter(name = genre1) :
                pass
            else :
                b = Genre(name = genre1)
                b.save()
        except :
            pass
        try :
            genre2 = artist.values_list('genre2', flat = True)[0]
            genre2 = genre2.strip()
            if Genre.objects.filter(name = genre2) :
                pass
            else :
                b = Genre(name = genre2)
                b.save()
        except :
            pass
        try :
            genre3 = artist.values_list('genre3', flat = True)[0]
            genre3 = genre3.strip()
            if Genre.objects.filter(name = genre3) :
                pass
            else :
                b = Genre(name = genre3)
                b.save()
        except :
            pass
        try :
            genre4 = artist.values_list('genre4', flat = True)[0]
            genre4 = genre4.strip()
            if Genre.objects.filter(name = genre4) :
                pass
            else :
                b = Genre(name = genre4)
                b.save()
        except :
            pass
        try :
            genre5 = artist.values_list('genre5', flat = True)[0]
            genre5 = genre5.strip()
            if Genre.objects.filter(name = genre5) :
                pass
            else :
                b = Genre(name = genre5)
                b.save()
        except :
            pass
        try :
            genre6 = artist.values_list('genre6', flat = True)[0]
            genre6 = genre6.strip()
            if Genre.objects.filter(name = genre6) :
                pass
            else :
                b = Genre(name = genre6)
                b.save()
        except :
            pass
        try :
            genre7 = artist.values_list('genre7', flat = True)[0]
            genre7 = genre7.strip()
            if Genre.objects.filter(name = genre7) :
                pass
            else :
                b = Genre(name = genre7)
                b.save()
        except :
            pass
        try :
            genre8 = artist.values_list('genre8', flat = True)[0]
            genre8 = genre8.strip()
            if Genre.objects.filter(name = genre8) :
                pass
            else :
                b = Genre(name = genre8)
                b.save()
        except :
            pass
        try :
            genre9 = artist.values_list('genre9', flat = True)[0]
            genre9 = genre9.strip()
            if Genre.objects.filter(name = genre9) :
                pass
            else :
                b = Genre(name = genre9)
                b.save()
        except :
            pass

insert_genre()
