import django
django.setup()
import lxml.html
from time import sleep
from .models import Songs


def get_songs_url():
    root = lxml.html.parse('http://got-djent.com/releases').getroot()
    for k in range(1, 21):
        title = root.xpath(
            '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[1]/a/span'.format(k))
        t = title[0].text
        artist = root.xpath(
            '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[3]/a'.format(k))
        a = artist[0].text
        base_url = root.xpath(
            '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[1]/a'.format(k))
        base_url = base_url[0].attrib
        base_url = base_url['href']
        u = "http://got-djent.com" + base_url
        Songs.objects.filter(artist=a, title=t).update(url=u)
    p = 0
    for c in range(1, 189):
        root = lxml.html.parse(
            'http://got-djent.com/releases?page={}'.format(c)).getroot()
        for k in range(1, 21):
            title = root.xpath(
                '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[1]/a/span'.format(k))
            t = title[0].text
            artist = root.xpath(
                '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[3]/a'.format(k))
            try:
                a = artist[0].text
            except:
                pass
            base_url = root.xpath(
                '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[1]/a'.format(k))
            base_url = base_url[0].attrib
            base_url = base_url['href']
            u = "http://got-djent.com" + base_url
            Songs.objects.filter(artist=a, title=t).update(url=u)
        p += 1
        print("URLを追加したページ数は")
        print(p)
        print("です。")
        print("休憩")
        sleep(1)
    print("追加終了")


get_songs_url()
