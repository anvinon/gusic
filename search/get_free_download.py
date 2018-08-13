import django
django.setup()
import lxml.html
from time import sleep
from .models import Songs


def f_download():
    root = lxml.html.parse(
        'http://got-djent.com/releases/free_download').getroot()
    for k in range(1, 11):
        for j in range(1, 3):
            artist = root.xpath(
                '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[{}]/div[3]/span/a'.format(k, j))
            a = artist[0].text
            title = root.xpath(
                '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[{}]/div[4]/span/a/span'.format(k, j))
            t = title[0].text
            url = root.xpath(
                '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[{}]/div[4]/span/a'.format(k, j))
            base_url = url[0].attrib
            base_url = base_url['href']
            u = "http://got-djent.com" + base_url
            Songs.objects.filter(artist=a, title=t).update(url=u)
    p = 0
    for c in range(1, 189):
        root = lxml.html.parse(
            'http://got-djent.com/releases/free_download?page={}'.format(c)).getroot()
        for k in range(1, 11):
            for j in range(1, 3):
                artist = root.xpath(
                    '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[{}]/div[3]/span/a'.format(k, j))
                a = artist[0].text
                title = root.xpath(
                    '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[{}]/div[4]/span/a/span'.format(k, j))
                t = title[0].text
                url = root.xpath(
                    '//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[{}]/div[4]/span/a'.format(k, j))
                base_url = url[0].attrib
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


f_download()
