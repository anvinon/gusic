from django.conf.urls import url
from . import views
from django.urls import include, path

app_name = 'search'
urlpatterns = [
    path('', views.index),
    path('index', views.index),    
    path('add', views.add),
    path('song', views.song),
    path('jump', views.jump),
    path('other_artist', views.other_artist, name='other_artist'),
    path('', views.other_artist, name='other_artist'),
    path('memo/<int:search_id>', views.memo, name='memo'),
    
]