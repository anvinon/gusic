import django
django.setup()
from search.models import Artist


def del_newline():
    for r in range(10215, 12731):
        artist_query = Artist.objects.filter(id=r)
        genre = artist_query.values_list('genre1', flat=True)[0]
        print(genre)
        genre = genre.strip("\n")
        Artist.objects.filter(id=r).update(genre1=genre)


del_newline()
