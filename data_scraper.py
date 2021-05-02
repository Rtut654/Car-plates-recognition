import json 
import requests 
import urllib3
from urllib import request
from bs4 import BeautifulSoup

names=['российские авто 1','машины с российскими номерами 2','авто в россии 1',
'авто в москве 1','авто на российских дорогах 1','автомобили в томске 1',
'автомобили в томске 1','авто в москве 6','автомобили в иркутске','авто в россии один']

t=252
for x in names[:1]:
  query=x
  query=request.quote(query.encode('cp1251'))
  query=  '+'.join(query.split()) 
  url="https://yandex.ru/search/xml?user=time221&key=03.113747997:7eb9d0f6f07ea85ae2259e4b1b8deb3c&text="+query+"&from=tabbar&groupby=attr%3Dd.mode%3Ddeep.groups-on-page%3D100.docs-in-group%3D3"
  # url="https://yandex.com/search/xml?user=rtut654&key=03.114054647:74e0993f14535cb06bb56014df9cc8f3&query=" +
  # query+"&l10n=en&sortby=tm.order%3Dascending&filter=none&groupby=attr%3Dd.mode%3Ddeep.groups-on-page%3D100.docs-in-group%3D"
  header={'User-Agent':"MMozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/76.0.3809.100 Chrome/76.0.3809.100 Safari/537.36"}
  http = urllib3.PoolManager()
  req = http.request(method='get',url=url,headers=header)
  soup = BeautifulSoup(req.data)
  print(url)

  n=1
  listimg=[]
  for i in range(n):
    listimg.append(str(soup.find_all("div",{"class":"serp-item serp-item_type_search serp-item_group_search serp-item_pos_"+str(i)+ " serp-item_scale_yes justifier__item i-bem"})))
    print()


  #нужно поиграться со split-ами
  k=0
  purelist=[]
  for i in range(n):
    try:
      purelist.append(listimg[i].split('origin')[1].split('"url"')[1][2:-25])
    except:
      k=k+1
  print(k)    

  # purelist # just to look at the list of links
  # !rm /content/gdrive/My\ Drive/download/*  #отчистка папки на drive
  for i in range(n):
    # try:
        with open('/data/'+str(t), 'wb') as img:
            response = requests.get(purelist[i], stream=True)
            img.write(response.content)
            t=t+1
    # except:
    #   print(1)         
