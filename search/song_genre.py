import django
from lxml.html import find_rel_links
django.setup()
import lxml.html
from time import sleep
from .models import Songs
import requests


def song_genre():
    root = lxml.html.parse('http://got-djent.com/releases').getroot()
    for a in range(1, 21):
        path = root.xpath(
            '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[1]/a'.format(a))
        base_url = path[0].attrib['href']
        url = "http://got-djent.com" + base_url
        tree = requests.get(url)
        tree = lxml.html.fromstring(tree.content)
        for x in tree.find_rel_links('tag'):
            print(lxml.html.tostring(x))
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[1]/a')
            title = tree.xpath('//*[@id="content-header"]/h1')
            t = title[0].text
            Songs.objects.filter(title=t).update(genre1=genre[0].text)
        except:
            pass
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[2]/a')

            Songs.objects.filter(title=t).update(genre2=genre[0].text)
        except:
            pass
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[3]/a')
            title = tree.xpath('//*[@id="content-header"]/h1')
            t = title[0].text
            Songs.objects.filter(title=t).update(genre3=genre[0].text)
        except:
            pass
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[4]/a')
            Songs.objects.filter(title=t).update(genre4=genre[0].text)
        except:
            pass
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[5]/a')
            Songs.objects.filter(title=t).update(genre5=genre[0].text)
        except:
            pass
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[6]/a')
            Songs.objects.filter(title=t).update(genre6=genre[0].text)
        except:
            pass
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[7]/a')
            Songs.objects.filter(title=t).update(genre7=genre[0].text)
        except:
            pass
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[8]/a')
            Songs.objects.filter(title=t).update(genre2=genre[8].text)
        except:
            pass
        try:
            genre = tree.xpath(
                '//*[@id="node-64643"]/div/div[1]/div[2]/ul/li[9]/a')
            Songs.objects.filter(title=t).update(genre2=genre[9].text)
        except:
            pass


#       p += 1
#         print("ジャンルを追加したページ数は")
#         print(p)
#         print("です。")
#         print("休憩")
#         sleep(1)
    print("追加終了")


song_genre()
