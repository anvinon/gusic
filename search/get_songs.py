import django
django.setup()
import lxml.html
from time import sleep
from .models import Songs

def get_songs():
    root = lxml.html.parse('http://got-djent.com/releases').getroot()
    for i in range(1, 21) :
        title = root.xpath('//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[1]/a/span'.format(i))            
        t = title[0].text
        artist = root.xpath('//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[3]/a'.format(i))
        a = artist[0].text
        s = Songs(artist = a, title = t)
        s.save()
    p = 0
    for k in range(1, 189) :
        root = lxml.html.parse('http://got-djent.com/releases?page={}'.format(k)).getroot()
        for i in range(1, 21) :
            title = root.xpath('//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[1]/a/span'.format(i))            
            t = title[0].text
            artist = root.xpath('//*[@id="content-area"]/div/div[2]/table/tbody/tr[{}]/td[3]/a'.format(i))
            try :
                a = artist[0].text
            except : 
                pass
            s = Songs(artist = a, title = t)
            s.save()
        p += 1
        print("取得したページ数は")
        print(p)
        print("です。")     
        print("休憩")
        sleep(1)   
    print("スクレイピング終了")
    
get_songs()